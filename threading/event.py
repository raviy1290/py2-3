import time
from threading import Event, Thread

def waiter(event, nloops):
	for i in range(nloops):
		print((i+1), 'Waiting for the flag to be set')
		event.wait() # Blocks until the flag becomes true.
		print('Wait complete at:', time.ctime())
		event.clear() # Resets the flag.
		print()

def setter(event, nloops):
	for i in range(nloops):
		time.sleep(1) # Sleeps for some time.
		event.set()

threads = []
nloops = 5
event = Event()

threads.append(Thread(target=waiter, args=(event, nloops)))
threads[-1].start()
threads.append(Thread(target=setter, args=(event, nloops)))
threads[-1].start()

for thread in threads:
    thread.join()

print('All done.')