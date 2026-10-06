import sqlite3

def authenticate(token: str) -> bool:
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    query = "SELECT * FROM tokens WHERE t = '" + token + "'"
    cursor.execute(query)
    return False