import numpy as np
import ArrayStack
#import BinaryTree
#import ChainedHashTable
#import DLList
#import operator


class Calculator:
    def __init__(self):
        self.dict = None #ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        # todo
        array_stack = ArrayStack.ArrayStack()
        for j in s:
            if j =='(':
                array_stack.push('(')
            elif j == ')':
                try:
                    array_stack.pop()
                except IndexError:
                    return False
                
        stack_size = array_stack.size()

        if stack_size == 0:
            return True
        else:
            return False

    def build_parse_tree(self, exp: str) -> str:
        # todo
        pass
    

    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        # todo
        pass

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)
