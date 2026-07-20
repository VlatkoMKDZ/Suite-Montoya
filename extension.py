# -*- coding: utf-8 -*-
from burp import IBurpExtender, IContextMenuFactory
from javax.swing import JMenu, JMenuItem
from java.util import ArrayList
from ui import TokenAttackAdvisorFrame

class BurpExtender(IBurpExtender, IContextMenuFactory):
    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        callbacks.setExtensionName('Token Attack Advisor')
        callbacks.registerContextMenuFactory(self)
        self.frame = TokenAttackAdvisorFrame(callbacks)
        callbacks.printOutput('Token Attack Advisor loaded')

    def createMenuItems(self, invocation):
        menu = JMenu('Token Attack Advisor')
        item = JMenuItem('Analyze Selected Request', actionPerformed=lambda event: self.analyze_selected(invocation))
        menu.add(item)
        top = JMenu('Extensions')
        top.add(menu)
        items = ArrayList()
        items.add(top)
        return items

    def analyze_selected(self, invocation):
        messages = invocation.getSelectedMessages()
        if not messages:
            self.callbacks.printError('No HTTP request selected')
            return
        self.frame.analyze_message(messages[0])
        self.frame.setVisible(True)
