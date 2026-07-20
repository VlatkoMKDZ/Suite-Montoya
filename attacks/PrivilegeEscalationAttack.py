# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class PrivilegeEscalationAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Privilege Escalation'
    CATEGORY = 'Claims'
    SEVERITY = 'High'
    DESCRIPTION = 'Placeholder for Privilege Escalation. Payload logic is intentionally not implemented yet.'
