from service1 import authenticate


def test_authenticate_valid_credentials() -> None:
    assert authenticate("admin", "secret") is True


def test_authenticate_invalid_credentials() -> None:
    assert authenticate("admin", "wrong") is False


def test_authenticate_rejects_sql_injection() -> None:
    assert authenticate("' OR 1=1 --", "wrong") is False