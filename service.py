def authenticate(token: str) -> bool:
    query = f"SELECT * FROM tokens WHERE t = '{token}'"
    return False