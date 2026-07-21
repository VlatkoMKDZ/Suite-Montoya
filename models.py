# -*- coding: utf-8 -*-
"""Data models for Token Attack Advisor."""

class JwtData(object):
    def __init__(self, token='', header=None, payload=None, signature='', raw_parts=None, error=None):
        self.token = token
        self.header = header or {}
        self.payload = payload or {}
        self.signature = signature
        self.raw_parts = raw_parts or []
        self.error = error

    def is_valid(self):
        return self.error is None and len(self.raw_parts) == 3


class AttackResult(object):
    def __init__(self, attack, original_jwt='', modified_jwt='', request=None, metadata=None,
                 original_request='', modified_request='', modified_header=None, modified_payload=None,
                 mutation_summary='', payload_used='', expected_result=''):
        self.attack = attack
        self.attack_name = attack.get_name() if attack else ''
        self.original_jwt = original_jwt
        self.modified_jwt = modified_jwt
        self.original_request = original_request
        self.modified_request = modified_request if modified_request is not None else request
        self.request = self.modified_request
        self.modified_header = modified_header or {}
        self.modified_payload = modified_payload or {}
        self.mutation_summary = mutation_summary
        self.payload_used = payload_used
        self.expected_result = expected_result or (attack.expected_result() if attack else '')
        self.metadata = metadata or {}
        self.response = None
        self.status = 'Generated'
        self.http_status = ''
        self.length = ''
        self.time_ms = ''
        self.verdict = 'Not run'
        self.verified = False
        self.diff = ''


class LogEntry(object):
    def __init__(self, level, message):
        self.level = level
        self.message = message
