from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        # todo
        if  i < 0 or i > self.n:
            return None

        if i < (self.n/2):
            p = self.dummy.next
            for j in range(i):
                p = p.next
        
        else: 
            p = self.dummy
            for j in range(self.n - i):
                p = p.prev
        
        return p

    def get(self, i) -> object:
        # todo
        if i < 0 or i > self.n:
            raise Exception
        
        return self.get_node(i).x

    def set(self, i: int, x: object) -> object:
        # todo
        if i < 0 or i > self.n:
            raise Exception
        
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w: Node, x: object) -> Node:
        # todo
        if w == None:
            return Exception
        
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u
        u.prev.next = u
        self.n += 1

    def add(self, i: int, x: object):
        # todo
        if i < 0 or i > self.n:
            return Exception
        
        return self.add_before(self.get_node(i),x)

    def _remove(self, w: Node):
        # todo
        if self.n == 0:
            raise IndexError()
        
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int):
        if i < 0 or i > self.n:  raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        # todo
        cleaned_string = []
        current = self.dummy.next

        while current != self.dummy:
            if str(current.x).isalnum():
                cleaned_string.append(str(current.x).lower())
            current = current.next

        return cleaned_string == cleaned_string[::-1]

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
    
    def reverse(self):
        current = self.dummy
        for i in range(self.n + 1):
            current.next, current.prev = current.prev, current.next
            current = current.prev
