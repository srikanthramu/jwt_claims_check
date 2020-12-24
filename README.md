# Utility to check missing claims from standards
Standards such as rfc7519 or OpenID Connect Core 1.0 has defined a set of standard claims for JWT.
This utility checks for missing claims from the input decoded jwt.

Usage:
    decoded_jwt = {'sub': 'subject', 'exp': 1608795899}
    #Test missing registered jwt claims
    missing_claims = get_missing_jwt_claims(decoded_jwt)
    print(f"Missing JWT registered claims: {missing_claims}")

    #Test missing standard ID token claims
    missing_claims = get_missing_id_token_claims(decoded_jwt)
    print(f"Missing ID token claims: {missing_claims}")
 
 Tested with Python 3.7.3
