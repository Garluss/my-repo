class Bil:
    def __init__(self):
        self.motor_aktivert = False

    def start_motor(self):
        self.motor_aktivert = True
    
    def stopp_motor(self):
        self.motor_aktivert = False