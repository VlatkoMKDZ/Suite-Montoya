# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class InvalidAudienceAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Invalid Audience'
    CATEGORY = 'Claims'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Placeholder for Invalid Audience. Payload logic is intentionally not implemented yet.'
