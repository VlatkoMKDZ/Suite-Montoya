# -*- coding: utf-8 -*-
from utils import string_to_bytes

class RepeaterSender(object):
    def __init__(self, callbacks):
        self.callbacks = callbacks

    def send(self, service, attack_result):
        if not service or not attack_result or not attack_result.request:
            return False
        self.callbacks.sendToRepeater(
            service.getHost(), service.getPort(), service.getProtocol() == 'https',
            string_to_bytes(attack_result.request), attack_result.attack.get_name())
        return True
