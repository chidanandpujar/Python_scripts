try:
    n = int(input("Enter number:"))
    m = 100/n
except ValueError:
    print("Value is not integer type")
except ZeroDivisionError:
    print("Device by Zero attempted")
else:
    print("Result=",n)
