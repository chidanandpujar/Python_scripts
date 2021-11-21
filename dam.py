import threading
import time
def daemon():
    print("daemon thread start")
    time.sleep(2)
    print("Finishing daemon thread")

def normalthread():
    print("Regular thread start")
    print("Regular thread end")

d = threading.Thread(target=daemon, name="daemon", daemon=True)
n = threading.Thread(target=normalthread, name="normal")
d.start()
n.start()
