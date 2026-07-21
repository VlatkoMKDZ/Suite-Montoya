# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class AlgorithmHs256Attack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Algorithm Confusion (RS256→HS256)'
    CATEGORY = 'Algorithm Confusion'
    SEVERITY = 'High'
    DESCRIPTION = 'Placeholder for Algorithm Confusion (RS256→HS256). Payload logic is intentionally not implemented yet.'
