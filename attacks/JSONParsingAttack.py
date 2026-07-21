# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class JSONParsingAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'JSON Parsing'
    CATEGORY = 'Parsing'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Placeholder for JSON Parsing. Payload logic is intentionally not implemented yet.'
