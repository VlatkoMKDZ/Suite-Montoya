# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class X5CAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'X5C'
    CATEGORY = 'Certificate'
    SEVERITY = 'High'
    DESCRIPTION = 'Placeholder for X5C. Payload logic is intentionally not implemented yet.'
