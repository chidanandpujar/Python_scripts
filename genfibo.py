def genfibo(max):
    p,c = 0,1
    while (c < max):
        yield c
        p,c = c,p+c

if (__name__ == "__main__"):
    for f in genfibo(100):
        print(f)
