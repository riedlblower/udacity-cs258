from queue_test import *

def test():
    ###Your code here.
    q=Queue(2)
    succeeded=q.enqueue(500000)
    assert succeeded
    value=q.dequeue()
    assert value==500000
    
    q=Queue(50)
    for i in range(50):
        succeeded=q.enqueue(i)
        assert succeeded

    q=Queue(2)
    succeeded=q.enqueue(10)
    assert succeeded
    assert not q.empty()
    value = q.dequeue()
    assert value == 10
        
    q=Queue(2)
    value = q.dequeue()
    assert value == None
    
    q=Queue(2)
    for i in range(2):
        succeeded=q.enqueue(i)
        assert succeeded
    return

