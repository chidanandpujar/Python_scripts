class M:
    def regular(self):
        print("regular method")
    @staticmethod
    def staty():
        print("static method")
    @classmethod
    def classy(cls):
        print("class method")

m1 = M()
m1.regular()
M.staty()
m1.staty()
M.classy()
m1.classy()
