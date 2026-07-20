# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class EmptyTokenAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Empty Token'
    CATEGORY = 'Token Handling'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Placeholder for Empty Token. Payload logic is intentionally not implemented yet.'
