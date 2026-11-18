from password_validator import is_valid_password


def test_valid_password():
    assert is_valid_password("Secure123") is True


def test_too_short():
    assert is_valid_password("Sec123") is False


def test_missing_uppercase():
    assert is_valid_password("secure123") is False


def test_missing_lowercase():
    assert is_valid_password("SECURE123") is False


def test_missing_digit():
    assert is_valid_password("SecureABC") is False


def test_empty_password():
    assert is_valid_password("") is False