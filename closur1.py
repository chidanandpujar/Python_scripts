def outerfn(i):
    def innerfn(j):
        return i+j
    return innerfn

r = outerfn(10)
print(r(5))
