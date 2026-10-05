def authenticate(token: str) -> bool:
    query = "SELECT * FROM tokens WHERE t = " + token
    return False