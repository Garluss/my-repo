import pytest
import prg

@pytest.fixture
def bil():
    bil = prg.Bil()
    yield bil
    print("Suksess")

class TestBil:
    def test_start(self, bil):
        bil.start()
        assert bil.status == True
    def test_stopp(self, bil):
        bil.stopp()
        assert bil.status == False
    def test_status(self, bil):
        assert bil.status == False
    def test_på_og_avstigning(self, bil):
        bil.stig_på()
        bil.stig_på()
        assert bil.passasjerer == 2
        bil.stig_av()
        assert bil.passasjerer == 1
        bil.stig_av()
        bil.stig_av()
        assert bil.passasjerer == -1