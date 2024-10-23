from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()  # NOTE: DLLDeque implements the Deque interface but also inherits all methods from DLList 

    def add(self, x : object):
        """
        adds an element to the end of this max queue
        INPUT: x the element to add
        """
        u = self.Node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1

        while self.max_deque.size() > 0 and self.max_deque.get(self.max_deque.size() - 1) < x:
            self.max_deque.remove_last()
        
        # Adding new element to max_deque
        self.max_deque.add_last(x)
        return True

    def remove(self) -> object:
        """
        removes and returns the element at the head of the max queue
        """
        if self.n == 0 :
            raise IndexError()
        
        temp = self.head.x

        if self.n == 1:
            self.head == None 
            self.last == None
        else:
            self.head = self.head.next

        self.n -= 1

        if temp == self.max_deque.get(0):
            self.max_deque.remove_first()

        return temp

    def max(self):
        """
        returns the maximum element stored in the queue
        """
        return self.max_deque.get(0)