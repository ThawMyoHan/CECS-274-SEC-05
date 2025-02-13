import numpy as np
from Interfaces import Queue

class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)
        
    def new_array(self, n: int) ->np.array:
        return np.zeros(n, object)
    
    def resize(self):
        '''
            Resize the array
        '''
        new_cap = max(1, 2 * self.n)
        resizing = self.new_array(new_cap)

        for k in range(0, self.n):
            resizing[k] = self.a[(self.j + k) % len(self.a)]
        
        self.a = resizing
        self.j = 0

    
    def add(self, x : object) :
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        if len(self.a) == self.n:
            self.resize()
        
        last_index = (self.j + self.n) % len(self.a)
        self.a[last_index] = x
        self.n += 1
        return True

    def remove(self) -> object :
        '''
            remove the first element in the queue
        '''
        if self.n <= 0:
            raise IndexError("remove from empty queue")
        
        x = self.a[self.j % len(self.a)]
        self.j = (self.j + 1) % len(self.a)
        self.n -= 1
        if len(self.a) >= 3 * self.n:
            self.resize()

        return x

    def size(self) :
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x
