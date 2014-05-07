import array
import random

# Although this specific Queue class has bugs spread
# throughout the code, do not modify the class.
class Queue:
    
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max - 1
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        x = x % 1000
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):            
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self
                    .size==0) or (self.size==self.max)    



def random_test():
	q = Queue(5000)
	num_tests = 10000
	tuple_list = []
	for i in range (0,num_tests):
		number = random.randrange(1,10)
		if (random.random() < 0.5):
			try:
				q.enqueue(number)
				q.checkRep()
				#print "enqueue Good" 
				tuple_list.append((number,0))
			except:
				tuple_list.append((number,1))
				#print "enqueue Bad"
		else:
			try:
				q.dequeue()
				q.checkRep()
				#print "dequeue Good"
				tuple_list.append(('dq',0))
			except:
				tuple_list.append(('dq',1))
				#print "dequeue Bad"	
#	print tuple_list
	return tuple_list
	
random_test()
