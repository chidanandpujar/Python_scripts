file = open("abc","w")
try:
    file.write("Testing")
    file.write("123")
except Exception as e:
    print("Exception",type(e))
finally:
    file.close()
