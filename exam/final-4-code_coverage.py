# coverage erase; coverage run code_coverage.py ; coverage html -i
# firefox htmlcov/code_coverage.html 


# Enhanced Queue class
class Queue:
    
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = {}

    def __str__(self):
        return str(self.data)

    def clear(self):       
        self.__init__(self.max)

    def empty(self):       
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if type(x) is not int and type(x) is not str and type(x) is not bool:
            return False
        if self.size == self.max:
            return False
        
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:           
            self.tail = 0
        return True

    def enqueueall(self, c):
        if type(c) is tuple or type(c) is list:
            if not self.size + len(c) > self.max:
                for itm in c:
                    self.enqueue(itm)
                return True
        return False

    def dequeue(self):
        if self.size == 0:           
            return None
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
            assert (self.size==0) or (self.size==self.max)


# Provide full statement and parameter value coverage of the Queue class
def test():
	q = Queue(5)
	q.checkRep()
	assert q.empty()
	q.dequeue()
	q.checkRep()
	q.clear()
	q.checkRep()
	q.full()
	q.checkRep()
	q.enqueue(2)
	q.checkRep()
	q.enqueue((2,3))
	q.checkRep()
	q.enqueue(True)
	q.checkRep()
	q.enqueue('a')
	q.checkRep()
	q.enqueue('*')
	q.checkRep()
	q.enqueue(4)
	q.checkRep()
	q.enqueue(6)
	q.checkRep()
	q.dequeue()
	q.checkRep()
	print q
	q.enqueueall((2,3))
	q.dequeue()
	q.enqueueall((4,5))
	print q	
	q.dequeue()
	q.dequeue()
	q.dequeue()
	q.dequeue()
	q.dequeue()
	q.dequeue()
	print q
	return

test()
    
