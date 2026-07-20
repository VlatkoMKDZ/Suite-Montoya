# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class UTF8TypoAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'UTF8 Typo'
    CATEGORY = 'Parsing'
    SEVERITY = 'Low'
    DESCRIPTION = 'Placeholder for UTF8 Typo. Payload logic is intentionally not implemented yet.'
