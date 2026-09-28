def authenticate(token: str) -> bool:
    # Vulnerabilità SAST (bloccante) + mancato rispetto del test logico
    query = "SELECT * FROM tokens WHERE t = '%s'" % token
    return False