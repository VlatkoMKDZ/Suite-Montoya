# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class ReplayAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Replay'
    CATEGORY = 'Session'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Placeholder for Replay. Payload logic is intentionally not implemented yet.'
