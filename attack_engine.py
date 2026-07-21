# -*- coding: utf-8 -*-
from attack_manager import AttackManager
from jwt_mutation_engine import JwtMutationEngine

class AttackEngine(object):
    def __init__(self, callbacks=None):
        self.callbacks = callbacks
        self.manager = AttackManager(callbacks)
        self.mutations = JwtMutationEngine()

    def load_attacks(self):
        return self.manager.load_attacks()

    def generate(self, jwt, request_text):
        results = []
        for attack in self.manager.applicable_attacks(jwt):
            result = attack.build_result(jwt, request_text)
            self._debug_generation(result)
            results.append(result)
        return results

    def _debug_generation(self, result):
        if not self.callbacks or not result:
            return
        original_auth = self.mutations.get_authorization_header(result.original_request)
        modified_auth = self.mutations.get_authorization_header(result.modified_request)
        lines = [
            'Token Attack Advisor mutation debug',
            'Attack Name: %s' % result.attack_name,
            'Original JWT: %s' % result.original_jwt,
            'Modified JWT: %s' % result.modified_jwt,
            'Original Authorization Header: %s' % original_auth,
            'Modified Authorization Header: %s' % modified_auth,
            'JWT changed: %s' % str(result.original_jwt != result.modified_jwt),
            'HTTP request changed: %s' % str(result.original_request != result.modified_request),
            'Authorization header changed: %s' % str(original_auth != modified_auth),
        ]
        try:
            self.callbacks.printOutput('\n'.join(lines))
        except Exception as exc:
            self.callbacks.printError('Token Attack Advisor debug logging failed: %s' % exc)
