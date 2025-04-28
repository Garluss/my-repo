from bil import Bil
import pytest as pt

@pt.fixture(scope="class")
def cls():
    print("\nClass Setup")
    yield
    print("\nClass Teardown")

@pt.fixture
def bil(cls):
    print("\nFunction Setup")
    bil = Bil()
    yield bil
    print("\nFunction Teardown")

class TestBil:
    def test_start_motor(self, bil): #argument nr. 2 er fixture
        print("Tester start")
        bil.start_motor()
        assert bil.motor_aktivert == True
    
    def test_stopp_motor(self, bil):
        print("Tester stopp")
        bil.stopp_motor()
        assert bil.motor_aktivert == False
