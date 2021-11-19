wlines = [ "Prabhu\n", "Gudi\n"]
fd = open("linesfile", "w")
fd.writelines(wlines)
fd.close()
