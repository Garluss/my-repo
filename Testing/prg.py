class Bil:
    def __init__(self):
        self.status = False
        self.passasjerer = 0
    def start(self):
        self.status = True
    def stopp(self):
        self.status = False
    def stig_på(self):
        self.passasjerer += 1
    def stig_av(self):
        self.passasjerer -= 1