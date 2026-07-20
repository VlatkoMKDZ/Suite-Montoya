# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class ModifiedExpirationAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Modified Expiration'
    CATEGORY = 'Claims'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Placeholder for Modified Expiration. Payload logic is intentionally not implemented yet.'
