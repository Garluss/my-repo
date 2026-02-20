import doofus
import pytest

def test_1():
    assert doofus.f(4) == -88

@pytest.mark.parametrize("x,f",[(4,-88),(-1,-3),(54,-23342938)])
def test_2(x,f):
    assert doofus.f(x) == f