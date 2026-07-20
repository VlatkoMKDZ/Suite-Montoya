# -*- coding: utf-8 -*-
from attack_base import JwtAttack

class PlaceholderAttack(JwtAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Placeholder'
    CATEGORY = 'JWT'
    DESCRIPTION = 'Attack placeholder. Payload generation is intentionally not implemented yet.'
    SEVERITY = 'Info'

    def get_name(self):
        return self.NAME

    def get_category(self):
        return self.CATEGORY

    def get_description(self):
        return self.DESCRIPTION

    def severity(self):
        return self.SEVERITY

    def expected_result(self):
        return 'A generated request is available for manual testing; no automated verdict yet.'
