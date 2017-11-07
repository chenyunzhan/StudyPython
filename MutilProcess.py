from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, time):
        super().__init__()
        self.time=time


    def run(self):
        start = time.time()
        time.sleep(self.time)
        stop = time.time()
        print("child spend %d"%(stop-start))


start = time.time()
for item in range(5):
    p = MyProcess(item+1)
    p.start()
stop = time.time()
print("parent spend %d" %(stop - start))
