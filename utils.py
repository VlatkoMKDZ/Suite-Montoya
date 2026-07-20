# -*- coding: utf-8 -*-
import base64
import json
import time

try:
    unicode
except NameError:
    unicode = str


def now_ms():
    return int(time.time() * 1000)


def bytes_to_string(data):
    if data is None:
        return ''
    try:
        return ''.join([chr(b & 0xff) for b in data])
    except TypeError:
        return str(data)


def string_to_bytes(value):
    if value is None:
        value = ''
    return value.encode('iso-8859-1')


def b64url_decode(value):
    value = value.replace('-', '+').replace('_', '/')
    padding = len(value) % 4
    if padding:
        value += '=' * (4 - padding)
    return base64.b64decode(value)


def b64url_encode(value):
    if isinstance(value, unicode):
        value = value.encode('utf-8')
    encoded = base64.urlsafe_b64encode(value).rstrip(b'=')
    if not isinstance(encoded, str):
        encoded = encoded.decode('ascii')
    return encoded


def json_dumps(value):
    return json.dumps(value, sort_keys=True, indent=2)


def clone_dict(value):
    return json.loads(json.dumps(value))
