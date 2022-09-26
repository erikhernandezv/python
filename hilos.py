import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print("() inicio".format(self.getName()))
        time.sleep(1)
        print("() terminado ".format(self.getName()))
        
        
if __name__=="__main__":
    for x in range(4):
        hilo=MyThread(name="Thread-()".format(x+1))
        hilo.start()
        time.sleep(.5)