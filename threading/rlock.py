# The standard LOCK doesnt know which thread is HOLDING it
# so even if same thread wants to acquire it it would BLOCKED 
# RLock()

import threading, time

lock = threading.Lock()

def fun1() :
	lock.acquire()
	time.sleep(1)
	lock.acquire()
	time.sleep(1)
	lock.release()


def fun2() :
	lock.acquire()
	time.sleep(1)
	lock.acquire()
	time.sleep(1)
	lock.release()

threads = []
for func in [fun1, fun2] :
	threads.append(threading.Thread(target=func))
	threads[-1].start()

for t in threads :
	t.join()

