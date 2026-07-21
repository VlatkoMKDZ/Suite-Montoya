# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class EmptyTokenAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Empty Token'
    CATEGORY = 'Token Handling'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Replace the bearer token with an empty Authorization bearer value.'

    def mutate(self, jwt):
        header = self.mutations.clone_header(jwt)
        payload = self.mutations.clone_payload(jwt)
        return '', header, payload, 'Removed token value from the Authorization bearer header.', 'Authorization: Bearer'

    def build_result(self, jwt, original_request):
        result = PlaceholderAttack.build_result(self, jwt, original_request)
        result.modified_request = self.mutations.build_empty_bearer_request(original_request)
        result.request = result.modified_request
        return result
