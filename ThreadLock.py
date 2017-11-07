import threading


num = 0
threads = []
mutex = threading.Lock()

def work():
    global num
    flag = mutex.acquire()
    if flag:
        for x in range(20000000):
            num+=1
        mutex.release()

    print(num)

for index in range(2):
    thread = threading.Thread(target=work)
    thread.start()
    threads.append(thread)
for item in threads:
    item.join()
print(num)



