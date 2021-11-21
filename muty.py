import time
import threading
from threading import  Lock
mylock = Lock()
def threadfn(data):
    mylock.acquire()
    if data == 3:
        time.sleep(2)
    print("Just coming out of lock",data)
    mylock.release()

i=0
while True:
    t = threading.Thread(target=threadfn,args=(i,))
    t.start()
    if i == 10:
        break
    i = i+1
