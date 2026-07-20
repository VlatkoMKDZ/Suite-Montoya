# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class JWKSAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'JWKS'
    CATEGORY = 'Key Discovery'
    SEVERITY = 'High'
    DESCRIPTION = 'Placeholder for JWKS. Payload logic is intentionally not implemented yet.'
