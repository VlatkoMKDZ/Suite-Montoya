# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class KidInjectionAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Kid Injection'
    CATEGORY = 'Key Discovery'
    SEVERITY = 'High'
    DESCRIPTION = 'Placeholder for Kid Injection. Payload logic is intentionally not implemented yet.'
