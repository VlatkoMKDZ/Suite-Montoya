# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class NullSignatureAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Null Signature'
    CATEGORY = 'Signature'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Placeholder for Null Signature. Payload logic is intentionally not implemented yet.'
