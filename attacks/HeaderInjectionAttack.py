# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class HeaderInjectionAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Header Injection'
    CATEGORY = 'Injection'
    SEVERITY = 'High'
    DESCRIPTION = 'Placeholder for Header Injection. Payload logic is intentionally not implemented yet.'
