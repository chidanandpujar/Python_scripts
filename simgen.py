def simplegen():
    yield("1")
    yield("2")
    yield("3")
    yield("4")
    yield("5")


mygen = simplegen()

for n in mygen:
    print(n)
