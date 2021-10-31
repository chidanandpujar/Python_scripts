def outerfn():
    def innerfn(i,j):
        return i+j
    return innerfn


r = outerfn()
print(r(1,2))
