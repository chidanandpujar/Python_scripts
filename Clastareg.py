class Stacla:
    """ static and class method demo"""
    ivar = 12345
    def regmethod(self):
        print("Regular method")
    @staticmethod
    def stamethod():
        print("Static method")
    @classmethod
    def clamethod(cls):
        print("class method")


#Stacla.regmethod()
Stacla.stamethod()
Stacla.clamethod()

s = Stacla()
s.regmethod()
s.stamethod()
s.clamethod()
