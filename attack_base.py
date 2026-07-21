# -*- coding: utf-8 -*-
from models import AttackResult
from jwt_mutation_engine import JwtMutationEngine

class JwtAttack(object):
    """Base class for every Token Attack Advisor attack module."""

    def __init__(self):
        self.mutations = JwtMutationEngine()

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

    def mutate(self, jwt):
        header = self.mutations.clone_header(jwt)
        payload = self.mutations.clone_payload(jwt)
        self.mutations.replace_header(header, 'taa_placeholder', self.get_name())
        token = self.mutations.rebuild_token(header, payload, jwt.signature)
        return token, header, payload, 'Added placeholder mutation marker.', 'taa_placeholder'

    def generate(self, jwt):
        """Return a modified JWT. Payload-specific logic lives in attack subclasses."""
        return self.mutate(jwt)[0] if jwt else ''

    def analyze(self, response):
        return 'Not analyzed'

    def expected_result(self):
        return 'Manual review required'

    def build_result(self, jwt, original_request):
        modified, header, payload, summary, payload_used = self.mutate(jwt)
        modified_request = self.mutations.build_modified_request(original_request, jwt.token, modified)
        return AttackResult(
            self,
            original_jwt=jwt.token if jwt else '',
            modified_jwt=modified,
            original_request=original_request,
            modified_request=modified_request,
            modified_header=header,
            modified_payload=payload,
            mutation_summary=summary,
            payload_used=payload_used,
            metadata={'description': self.get_description(), 'expected': self.expected_result()})
