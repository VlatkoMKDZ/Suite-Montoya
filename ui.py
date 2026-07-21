# -*- coding: utf-8 -*-
from javax.swing import (JFrame, JPanel, JSplitPane, JScrollPane, JTable, JTabbedPane,
    JTextArea, JButton, JToolBar, BorderFactory, ListSelectionModel)
from javax.swing.table import AbstractTableModel
from java.awt import BorderLayout
from jwt_parser import JwtParser
from attack_engine import AttackEngine
from repeater import RepeaterSender
from utils import bytes_to_string, string_to_bytes, now_ms
from response_analyzer import ResponseAnalyzer
from diff_engine import DiffEngine

class AttackTableModel(AbstractTableModel):
    COLUMNS = ['Status', 'Severity', 'Category', 'Attack', 'HTTP Status', 'Length', 'Time', 'Verdict', 'Verified']

    def __init__(self):
        self.rows = []

    def getRowCount(self):
        return len(self.rows)

    def getColumnCount(self):
        return len(self.COLUMNS)

    def getColumnName(self, index):
        return self.COLUMNS[index]

    def getValueAt(self, row, col):
        result = self.rows[row]
        values = [result.status, result.attack.severity(), result.attack.get_category(),
                  result.attack.get_name(), result.http_status, result.length,
                  result.time_ms, result.verdict, str(result.verified)]
        return values[col]

    def setRows(self, rows):
        self.rows = rows
        self.fireTableDataChanged()

class TokenAttackAdvisorFrame(JFrame):
    def __init__(self, callbacks):
        JFrame.__init__(self, 'Token Attack Advisor')
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        self.parser = JwtParser()
        self.engine = AttackEngine(callbacks)
        self.repeater = RepeaterSender(callbacks)
        self.response_analyzer = ResponseAnalyzer()
        self.diff_engine = DiffEngine()
        self.message = None
        self.service = None
        self.request_text = ''
        self.jwt = None
        self.results = []
        self._build_ui()
        self.setSize(1200, 800)

    def _build_ui(self):
        root = JPanel(BorderLayout())
        toolbar = JToolBar()
        for label, handler in [('Analyze', self.on_analyze), ('Generate Attacks', self.on_generate),
                               ('Run Selected', self.on_run_selected), ('Run Safe Tests', self.on_run_safe),
                               ('Send To Repeater', self.on_send_repeater), ('Export', self.on_export),
                               ('Settings', self.on_settings)]:
            toolbar.add(JButton(label, actionPerformed=handler))
        root.add(toolbar, BorderLayout.NORTH)

        self.model = AttackTableModel()
        self.table = JTable(self.model)
        self.table.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION)
        self.table.getSelectionModel().addListSelectionListener(lambda event: self.on_selection())

        self.tabs = JTabbedPane()
        self.overview = self._text_tab('Overview')
        self.decoded = self._text_tab('Decoded JWT')
        self.details = self._text_tab('Attack Details')
        self.generated_request = self._text_tab('Generated Request')
        self.generated_request.setEditable(True)
        self.response = self._text_tab('Response')
        self.diff = self._text_tab('Diff')
        self.payloads = self._text_tab('Payloads')
        self.history = self._text_tab('History')

        split = JSplitPane(JSplitPane.HORIZONTAL_SPLIT, JScrollPane(self.table), self.tabs)
        split.setDividerLocation(520)
        root.add(split, BorderLayout.CENTER)

        self.log = JTextArea()
        self.log.setEditable(False)
        panel = JPanel(BorderLayout())
        panel.add(root, BorderLayout.CENTER)
        log_scroll = JScrollPane(self.log)
        log_scroll.setBorder(BorderFactory.createTitledBorder('Log Console'))
        panel.add(log_scroll, BorderLayout.SOUTH)
        self.setContentPane(panel)

    def _text_tab(self, title):
        area = JTextArea()
        area.setEditable(False)
        self.tabs.addTab(title, JScrollPane(area))
        return area

    def log_line(self, message):
        self.log.append(message + '\n')

    def analyze_message(self, message):
        self.message = message
        self.service = message.getHttpService()
        self.request_text = bytes_to_string(message.getRequest())
        self.on_analyze(None)

    def on_analyze(self, event):
        token = self.parser.extract_token(self.request_text)
        self.jwt = self.parser.parse(token)
        self.overview.setText('Token found: %s\nStatus: %s' % (str(token is not None), self.jwt.error or 'Parsed'))
        self.decoded.setText(self.parser.pretty(self.jwt))
        self.log_line('Analyzed selected request')

    def on_generate(self, event):
        if not self.jwt or not self.jwt.is_valid():
            self.on_analyze(event)
        self.results = self.engine.generate(self.jwt, self.request_text) if self.jwt and self.jwt.is_valid() else []
        self.model.setRows(self.results)
        self.payloads.setText('Payload implementations are intentionally empty in this framework build.')
        self.history.append('Generated %d attack requests\n' % len(self.results))
        self.log_line('Generated %d attacks' % len(self.results))

    def selected_results(self):
        rows = self.table.getSelectedRows()
        if not rows:
            return []
        return [self.results[self.table.convertRowIndexToModel(row)] for row in rows]

    def on_selection(self):
        selected = self.selected_results()
        if not selected:
            return
        result = selected[0]
        self.details.setText('%s\n\n%s\n\nMutation: %s\nPayload Used: %s\nExpected: %s' % (
            result.attack.get_name(), result.attack.get_description(),
            result.mutation_summary, result.payload_used, result.attack.expected_result()))
        self.generated_request.setText(result.request or '')
        self.response.setText(bytes_to_string(result.response) if result.response else '')
        self.diff.setText(result.diff or '')

    def on_run_selected(self, event):
        for result in self.selected_results():
            start = now_ms()
            request = string_to_bytes(self.generated_request.getText() if len(self.selected_results()) == 1 else result.request)
            response = self.callbacks.makeHttpRequest(self.service, request)
            elapsed = now_ms() - start
            result.response = response.getResponse()
            info = self.helpers.analyzeResponse(result.response)
            summary = self.response_analyzer.summarize(info, result.response, elapsed)
            result.status = 'Run'
            result.http_status = summary['http_status']
            result.length = summary['length']
            result.time_ms = summary['time_ms']
            result.verdict = result.attack.analyze(result.response)
            result.diff = self.diff_engine.compare(None, summary['body'])
        self.model.fireTableDataChanged()
        self.on_selection()

    def on_run_safe(self, event):
        self.log_line('Safe-test filtering will be implemented with payload logic.')

    def on_send_repeater(self, event):
        for result in self.selected_results():
            self.repeater.send(self.service, result)
        self.log_line('Sent selected requests to Repeater')

    def on_export(self, event):
        self.log_line('Export placeholder: no file writer configured yet.')

    def on_settings(self, event):
        self.log_line('Settings placeholder')
