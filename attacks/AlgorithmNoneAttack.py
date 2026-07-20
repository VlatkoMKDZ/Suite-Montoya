# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class AlgorithmNoneAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Algorithm Confusion (RS256→none)'
    CATEGORY = 'Algorithm Confusion'
    SEVERITY = 'High'
    DESCRIPTION = 'Placeholder for Algorithm Confusion (RS256→none). Payload logic is intentionally not implemented yet.'
