# -*- coding: utf-8 -*-
import time
from _placeholder import PlaceholderAttack

class ModifiedExpirationAttack(PlaceholderAttack):
    IS_TOKEN_ATTACK = True
    NAME = 'Modified Expiration'
    CATEGORY = 'Claims'
    SEVERITY = 'Medium'
    DESCRIPTION = 'Set exp to the current time plus ten years, adding it when missing.'

    def mutate(self, jwt):
        header = self.mutations.clone_header(jwt)
        payload = self.mutations.clone_payload(jwt)
        new_exp = int(time.time()) + (10 * 365 * 24 * 60 * 60)
        self.mutations.replace_claim(payload, 'exp', new_exp)
        token = self.mutations.rebuild_token(header, payload, jwt.signature)
        return token, header, payload, 'Set exp to current time plus 10 years.', 'exp=%d' % new_exp
