from threading import Thread
import time
import threading 

g = 0
def add_one() :
	global g
	print(g, threading.current_thread().name)
	time.sleep(1)
	g += 1
	print(g, threading.current_thread().name)

def add_two() :
	global g
	print(g, threading.current_thread().name)
	time.sleep(1)
	g += 2
	print(g, threading.current_thread().name)

def add_three() :
	global g
	print(g, threading.current_thread().name)
	time.sleep(1)
	g += 3
	print(g, threading.current_thread().name)

lock = threading.Lock()

def add_one_locked() :
	lock.acquire()
	global g
	print(g, threading.current_thread().name)
	time.sleep(1)
	g += 1
	print(g, threading.current_thread().name)
	lock.release()

def add_two_locked() :
	lock.acquire()
	global g
	print(g, threading.current_thread().name)
	time.sleep(1)
	g += 2
	print(g, threading.current_thread().name)
	lock.release()

def add_three_locked() :
	lock.acquire()
	global g
	print(g, threading.current_thread().name)
	time.sleep(1)
	g += 3
	print(g, threading.current_thread().name)
	lock.release()


threads = []
for index, func in enumerate([add_one, add_two, add_three]):
   threads.append(Thread(target=func, name='thread-'+str(index)))
   threads[-1].start()	

for thread in threads :
	thread.join()

threads_locked = []
for index, func in enumerate([add_one_locked, add_two_locked, add_three_locked]):
   threads_locked.append(Thread(target=func, name='thread-l-'+str(index)))
   threads_locked[-1].start()	

for thread_l in threads_locked :
	thread_l.join()