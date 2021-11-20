import threading
def mythread():
    print("My thread")

threads=[]
for i in range(5):
    t = threading.Thread(target=mythread())
    threads.append(t)
    t.start()
