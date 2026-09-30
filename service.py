def authenticate(token: str) -> bool:
    query = f"SELECT * FROM tokens WHERE t = %s"
    return True
