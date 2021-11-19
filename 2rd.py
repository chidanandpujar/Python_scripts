fd = open('f',"r")
buffer = fd.read(2)
print("first 2 chars in f:",buffer)
fd.close()
