import threading
import time

num = 100

def fun1(num):
    num +=1
    print("%d"%num)

def fun2():
    print("%d"%num)

print("====%d"%num)

thread1 = threading.Thread(target=fun1, args=(num,))
thread1.start()

time.sleep(2)

thread2 = threading.Thread(target=fun2)
thread2.start()

print("====%d" % num)
