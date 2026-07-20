# -*- coding: utf-8 -*-
from utils import bytes_to_string

class ResponseAnalyzer(object):
    def summarize(self, response_info, response_bytes, elapsed_ms):
        body = bytes_to_string(response_bytes)
        return {
            'http_status': str(response_info.getStatusCode()) if response_info else '',
            'length': str(len(response_bytes) if response_bytes else 0),
            'time_ms': str(elapsed_ms),
            'body': body,
        }
