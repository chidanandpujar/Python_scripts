import threading
class testrun(threading.Thread):
    def run(self):
        print("Inside thread run\r")

t = testrun()
t.start()
t.join()
