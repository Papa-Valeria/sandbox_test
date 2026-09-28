from service import authenticate

def test_authenticate():
    assert authenticate("secret_valid_token") is True