# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class RaceConditionAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Race Condition'
    CATEGORY = 'Concurrency'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Placeholder for Race Condition. Payload logic is intentionally not implemented yet.'
