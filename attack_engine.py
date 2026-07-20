# -*- coding: utf-8 -*-
from attack_manager import AttackManager
from request_builder import RequestBuilder

class AttackEngine(object):
    def __init__(self, callbacks=None):
        self.manager = AttackManager(callbacks)
        self.builder = RequestBuilder()

    def load_attacks(self):
        return self.manager.load_attacks()

    def generate(self, jwt, request_text):
        results = []
        for attack in self.manager.applicable_attacks(jwt):
            modified = attack.generate(jwt)
            modified_request = self.builder.replace_token(request_text, jwt.token, modified)
            result = attack.build_result(jwt, modified_request)
            result.modified_jwt = modified
            results.append(result)
        return results
