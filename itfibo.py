def itfibo(max):
    p,c = 0,1
    while (c < max):
        print(c)
        p,c = c,p+c

if (__name__ == "__main__"):
    itfibo(100)
