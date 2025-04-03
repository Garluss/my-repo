import smidioppgave as s
import pytest

@pytest.mark.parametrize("p,res",[(0,"Ikke bestått"),(50,"Bestått"),(69,"Bestått"),(70,"Godt bestått"),(89,"Godt bestått"),(90,"Meget godt bestått"),(100,"Meget godt bestått"),(-1,"Ikke gyldig poengsum!")])
def test_1(p,res):
    assert s.karakter(p) == res

@pytest.mark.parametrize("p,res",[(0,"Ikke bestått"),(50,"Bestått"),(69,"Bestått"),(70,"Godt bestått"),(89,"Godt bestått"),(90,"Meget godt bestått"),(100,"Meget godt bestått"),(-1,"Ikke gyldig poengsum!")])
def test_2(p,res):
    assert s.karakter_ordnet(p) == res