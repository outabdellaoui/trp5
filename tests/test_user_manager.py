import pytest
from app.user_manager import create_user


def test_create_user():
    user = create_user("otman", "otman@example.com")
    assert isinstance(user, dict)
    assert user["username"] == "otman"
    assert user["email"] == "otman@example.com"


def test_create_user_missing_username():
    with pytest.raises(ValueError):
        create_user("", "email@example.com")