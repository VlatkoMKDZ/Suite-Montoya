# -*- coding: utf-8 -*-
"""Reusable JWT mutation helpers for Token Attack Advisor."""
import copy
import json
import re
from jwt_parser import JwtParser
from utils import b64url_encode

class JwtMutationEngine(object):
    def __init__(self):
        self.parser = JwtParser()

    def decode_token(self, token):
        return self.parser.parse(token)

    def encode_token(self, header, payload, signature):
        return self.rebuild_token(header, payload, signature)

    def clone_header(self, jwt):
        return copy.deepcopy(jwt.header if jwt else {})

    def clone_payload(self, jwt):
        return copy.deepcopy(jwt.payload if jwt else {})

    def replace_claim(self, payload, name, value):
        payload[name] = value
        return payload

    def remove_claim(self, payload, name):
        if name in payload:
            del payload[name]
        return payload

    def replace_header(self, header, name, value):
        header[name] = value
        return header

    def remove_header(self, header, name):
        if name in header:
            del header[name]
        return header

    def remove_signature(self):
        return ''

    def replace_signature(self, value):
        return value or ''

    def rebuild_token(self, header, payload, signature):
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        payload_json = json.dumps(payload, separators=(',', ':'), sort_keys=True)
        return '%s.%s.%s' % (b64url_encode(header_json), b64url_encode(payload_json), signature or '')

    def replace_token_in_http_request(self, request_text, original_token, modified_token):
        if not request_text or not original_token:
            return request_text
        return request_text.replace(original_token, modified_token, 1)

    def build_modified_request(self, request_text, original_token, modified_token):
        return self.replace_token_in_http_request(request_text, original_token, modified_token)

    def build_empty_bearer_request(self, request_text):
        if not request_text:
            return request_text
        pattern = re.compile(r'(?im)^(Authorization\s*:\s*Bearer)(?:\s+[^\r\n]*)?')
        return pattern.sub(r'\1', request_text, 1)
