import pytest

@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100
    
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100
    
@pytest.mark.skip
def test_less():
    num = 100
    assert num < 200
    
@pytest.mark.xfail
def test_notequal():
    num = 100
    assert num == 100
    