# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class RevocationAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Revocation'
    CATEGORY = 'Session'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Placeholder for Revocation. Payload logic is intentionally not implemented yet.'
