# Registered Claims - https://tools.ietf.org/html/rfc7519#section-4.1
JWT_REG_CLAIMS = {"iss", "sub", "aud", "exp", "nbf", "iat", "jti"}

# ID Token claims https://openid.net/specs/openid-connect-core-1_0.html#IDToken
ID_TOKEN_CLAIMS = {"iss", "sub", "aud", "exp", "nbf", "iat", "auth_time", "nonce", "acr", "amr", "azp", "jti"}


def get_missing_jwt_claims(decoded_jwt):
    return get_missing_claims(decoded_jwt, JWT_REG_CLAIMS)


def get_missing_id_token_claims(decoded_jwt):
    return get_missing_claims(decoded_jwt, ID_TOKEN_CLAIMS)


def get_missing_claims(decoded_jwt, std_claims):
    claim_set = set()
    for claim in decoded_jwt:
        claim_set.add(claim)
    return std_claims.difference(claim_set)
