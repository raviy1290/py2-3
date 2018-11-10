import threading, time

class Counter() :
	def __init__(self):
		self.value = 0
		self.lock = threading.Lock()

	def increment(self):
		with self.lock :
			self.value+=1

c = Counter()

def go():
	for i in range(100000) :
		c.increment()

# Run on two threads 

t1 = threading.Thread(target=go)
t1.start()

t2 = threading.Thread(target=go)
t2.start()

t1.join()
t2.join()

print(c.value)