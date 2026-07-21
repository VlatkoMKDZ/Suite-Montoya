# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class DelimiterAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Delimiter'
    CATEGORY = 'Parsing'
    SEVERITY = 'Low'
    DESCRIPTION = 'Placeholder for Delimiter. Payload logic is intentionally not implemented yet.'
