# -*- coding: utf-8 -*-
import os
import sys

class AttackManager(object):
    def __init__(self, callbacks=None):
        self.callbacks = callbacks
        self.attacks = []

    def load_attacks(self):
        base = os.path.dirname(os.path.abspath(__file__))
        attacks_dir = os.path.join(base, 'attacks')
        if attacks_dir not in sys.path:
            sys.path.insert(0, attacks_dir)
        self.attacks = []
        for filename in sorted(os.listdir(attacks_dir)):
            if not filename.endswith('.py') or filename.startswith('_'):
                continue
            module_name = filename[:-3]
            module = __import__(module_name)
            for value in module.__dict__.values():
                try:
                    if (hasattr(value, 'IS_TOKEN_ATTACK') and value.IS_TOKEN_ATTACK
                            and getattr(value, '__module__', None) == module_name):
                        self.attacks.append(value())
                except Exception:
                    pass
        return self.attacks

    def applicable_attacks(self, jwt):
        if not self.attacks:
            self.load_attacks()
        return [attack for attack in self.attacks if attack.is_applicable(jwt)]
