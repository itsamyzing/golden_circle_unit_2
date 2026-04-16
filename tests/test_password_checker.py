import pytest
from lib.password_checker import *

# Check that password is more than 8 characters

def test_password_longer_than_8_characters():
    password = PasswordChecker()
    result = password.check("abcdefghijk")
    assert result == True

# Test if password returns error message if less than 8 characters

def test_password_less_than_8_characters():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("abd")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."

# Test for a password that is 8 chacarcters long passes

def test_password_of_exactly_8_characters():
    password = PasswordChecker()
    result = password.check("abcdeghi")
    assert result == True