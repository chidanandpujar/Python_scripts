def mult( *args):
    t = 1
    for n in args:
        t = n * t
    print(t)

mult(1)
mult(1,2,3)
mult(1,2,3,4,5)
