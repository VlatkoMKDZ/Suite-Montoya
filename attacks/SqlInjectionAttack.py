# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class SqlInjectionAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'SQL Injection'
    CATEGORY = 'Injection'
    SEVERITY = 'High'
    DESCRIPTION = 'Placeholder for SQL Injection. Payload logic is intentionally not implemented yet.'
