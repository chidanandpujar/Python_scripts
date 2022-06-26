class cls:
    state = "ka"
    def behave(selfs):
        print("Behave inside")
    def ritty(self,x):
        print(x)
        return x
c1 = cls()
c1.behave()
print(c1.state)
c1.ritty(5)
