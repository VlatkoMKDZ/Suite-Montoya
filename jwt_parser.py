# -*- coding: utf-8 -*-
import json
import re
from models import JwtData
from utils import b64url_decode, json_dumps

AUTH_BEARER_RE = re.compile(r'(?im)^Authorization\s*:\s*Bearer\s+([^\s\r\n]+)')
JWT_RE = re.compile(r'[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]*')

class JwtParser(object):
    def extract_token(self, request_text):
        if not request_text:
            return None
        bearer = AUTH_BEARER_RE.search(request_text)
        if bearer:
            return bearer.group(1)
        match = JWT_RE.search(request_text)
        return match.group(0) if match else None

    def parse(self, token):
        if not token:
            return JwtData(error='No JWT token found')
        parts = token.split('.')
        if len(parts) != 3:
            return JwtData(token=token, raw_parts=parts, error='JWT must contain three parts')
        try:
            header = json.loads(b64url_decode(parts[0]))
            payload = json.loads(b64url_decode(parts[1]))
            return JwtData(token=token, header=header, payload=payload, signature=parts[2], raw_parts=parts)
        except Exception as exc:
            return JwtData(token=token, raw_parts=parts, error=str(exc))

    def pretty(self, jwt_data):
        if not jwt_data or not jwt_data.is_valid():
            return jwt_data.error if jwt_data else 'No JWT parsed'
        return 'Header:\n%s\n\nPayload:\n%s\n\nSignature:\n%s' % (
            json_dumps(jwt_data.header), json_dumps(jwt_data.payload), jwt_data.signature)
