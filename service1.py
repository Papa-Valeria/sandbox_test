import sqlite3


def authenticate(username: str, password: str) -> bool:
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE users (username TEXT, password TEXT)"
    )

    cursor.execute(
        "INSERT INTO users VALUES ('admin', 'secret')"
    )

    query = (
        "SELECT * FROM users "
        f"WHERE username = '{username}' "
        f"AND password = '{password}'"
    )

    cursor.execute(query)
    result = cursor.fetchone()

    connection.close()

    return result is not None