import threading
def mythread(arg):
    print("Finished simple thread!!\n",arg)

t = threading.Thread(target=mythread,args=(2,))
t.start()
t.join()
