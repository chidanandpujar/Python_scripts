import threading
def mythread():
    print("Finished simple thread!!\n")

t = threading.Thread(target=mythread())
t.start()
