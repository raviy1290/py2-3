import threading, time
aLock = threading.Lock()
bLock = threading.Lock()

print(id(aLock), id(bLock))

a = 1
b = 1

def thread1() :
	print("T1 starts...")
	aLock.acquire()
	time.sleep(5)

	bLock.acquire()
	time.sleep(5)

	a +=5
	b +=5

	bLock.release()
	aLock.release()

def thread2() :
	print("T1 starts...")
	bLock.acquire()
	time.sleep(5)

	aLock.acquire()
	time.sleep(5)

	a +=5
	b +=5	

	aLock.release()
	bLock.release()


t1 = threading.Thread(target=thread1)
t1.start()

t2 = threading.Thread(target=thread2)
t2.start()

t1.join()
t2.join()
