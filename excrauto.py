try:
    n = int(input("Enter a number:"))
    m = 100/n
except Exception as e:
    print("Exception", type(e))
else:
    print("Result=",m)
