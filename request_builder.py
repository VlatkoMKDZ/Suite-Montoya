# -*- coding: utf-8 -*-

class RequestBuilder(object):
    def replace_token(self, request_text, original_token, modified_token):
        if not request_text or not original_token:
            return request_text
        return request_text.replace(original_token, modified_token, 1)
