try:
    n = int(input("Enter a number:"))
    m = 100/n
except (ValueError,ZeroDivisionError):
    print("Either non integer entered or divide by zero")
else:
    print("Result=",m)
