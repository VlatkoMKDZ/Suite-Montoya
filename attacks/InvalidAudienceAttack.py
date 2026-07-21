# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class InvalidAudienceAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Invalid Audience'
    CATEGORY = 'Claims'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Replace the aud claim with invalid-audience.'

    def mutate(self, jwt):
        header = self.mutations.clone_header(jwt)
        payload = self.mutations.clone_payload(jwt)
        self.mutations.replace_claim(payload, 'aud', 'invalid-audience')
        token = self.mutations.rebuild_token(header, payload, jwt.signature)
        return token, header, payload, 'Replaced aud with invalid-audience.', 'aud=invalid-audience'
