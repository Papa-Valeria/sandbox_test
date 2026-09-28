def authenticate(token: str) -> bool:
    query = "SELECT * FROM tokens WHERE t = '%s'" % token
    return False
