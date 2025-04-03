import bmi
import pytest

@pytest.mark.parametrize("høyde,vekt,resultat",[(1.50,60,"Overvektig"),(2.10,92,"Normalvektig"),(1.40,89,"Fedme, grad 3")])
def test_1(høyde, vekt, resultat):
    assert bmi.klassifisering(høyde,vekt) == resultat