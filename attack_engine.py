# -*- coding: utf-8 -*-
from attack_manager import AttackManager

class AttackEngine(object):
    def __init__(self, callbacks=None):
        self.manager = AttackManager(callbacks)

    def load_attacks(self):
        return self.manager.load_attacks()

    def generate(self, jwt, request_text):
        results = []
        for attack in self.manager.applicable_attacks(jwt):
            results.append(attack.build_result(jwt, request_text))
        return results
