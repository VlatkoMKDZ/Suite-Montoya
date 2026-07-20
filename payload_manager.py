# -*- coding: utf-8 -*-

class PayloadManager(object):
    def __init__(self):
        self.payloads = {}

    def register(self, name, payload):
        self.payloads.setdefault(name, []).append(payload)

    def get(self, name):
        return self.payloads.get(name, [])
