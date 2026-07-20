# -*- coding: utf-8 -*-
from models import AttackResult

class JwtAttack(object):
    """Base class for every Token Attack Advisor attack module."""

    def get_name(self):
        raise NotImplementedError()

    def get_category(self):
        return 'JWT'

    def get_description(self):
        return 'Placeholder attack description.'

    def severity(self):
        return 'Info'

    def is_applicable(self, jwt):
        return jwt is not None and jwt.is_valid()

    def generate(self, jwt):
        """Return modified JWT placeholder. Payload logic intentionally not implemented yet."""
        return jwt.token if jwt else ''

    def analyze(self, response):
        return 'Not analyzed'

    def expected_result(self):
        return 'Manual review required'

    def build_result(self, jwt, request):
        modified = self.generate(jwt)
        return AttackResult(
            self,
            original_jwt=jwt.token if jwt else '',
            modified_jwt=modified,
            request=request,
            metadata={'description': self.get_description(), 'expected': self.expected_result()})
