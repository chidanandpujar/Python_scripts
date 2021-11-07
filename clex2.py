class cls:
    state="ka"
    def behave(self):
        print("Behave inside")
    def ritty(self,x):
        print(x)
        return x

c1 = cls()
c1.behave()
print(c1.state)
print(c1.behave)
c1.ritty(5)
