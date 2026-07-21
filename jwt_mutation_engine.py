# -*- coding: utf-8 -*-
"""Reusable JWT mutation helpers for Token Attack Advisor."""
import copy
import json
import re
from jwt_parser import JwtParser
from utils import b64url_encode

AUTHORIZATION_RE = re.compile(r'^(?P<name>Authorization\s*:\s*)(?P<scheme>Bearer)(?P<space>\s*)(?P<token>[^\r\n]*?)(?P<ending>\r\n|\n|\r)?$', re.I)
HEADER_END_RE = re.compile(r'\r\n\r\n|\n\n|\r\r')

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

    def split_headers_and_body(self, request_text):
        match = HEADER_END_RE.search(request_text or '')
        if not match:
            return request_text or '', '', ''
        return request_text[:match.start()], match.group(0), request_text[match.end():]

    def get_authorization_header(self, request_text):
        header_block, separator, body = self.split_headers_and_body(request_text)
        for line in header_block.splitlines(True):
            if line.lower().startswith('authorization:'):
                return line.rstrip('\r\n')
        return ''

    def replace_authorization_bearer_token(self, request_text, modified_token):
        header_block, separator, body = self.split_headers_and_body(request_text)
        lines = header_block.splitlines(True)
        rebuilt = []
        changed = False
        for line in lines:
            if not changed:
                match = AUTHORIZATION_RE.match(line)
                if match:
                    ending = match.group('ending') or ''
                    token_part = (' ' + modified_token) if modified_token else ''
                    rebuilt.append('%s%s%s%s' % (match.group('name'), match.group('scheme'), token_part, ending))
                    changed = True
                    continue
            rebuilt.append(line)
        if changed:
            return ''.join(rebuilt) + separator + body
        return None

    def replace_token_in_http_request(self, request_text, original_token, modified_token):
        modified_request = self.replace_authorization_bearer_token(request_text, modified_token)
        if modified_request is not None:
            return modified_request
        if not request_text or not original_token:
            return request_text
        return request_text.replace(original_token, modified_token, 1)

    def build_modified_request(self, request_text, original_token, modified_token):
        return self.replace_token_in_http_request(request_text, original_token, modified_token)

    def build_empty_bearer_request(self, request_text):
        modified_request = self.replace_authorization_bearer_token(request_text, '')
        return modified_request if modified_request is not None else request_text
