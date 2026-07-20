# -*- coding: utf-8 -*-

class DiffEngine(object):
    def compare(self, original_response, attack_response):
        if not original_response and not attack_response:
            return 'No responses available.'
        original_len = len(original_response or '')
        attack_len = len(attack_response or '')
        return 'Original length: %d\nAttack length: %d\nDelta: %+d' % (
            original_len, attack_len, attack_len - original_len)
