import pytest

str = "12name"
def capitalize(str):
    return str.upper()

def test_validate_and_capitalize():
    with pytest.raises(Exception) as e:
        capitalize(str)
        assert "e.type" == ValueError
