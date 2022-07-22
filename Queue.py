from _collections import deque
stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
for _ in range(3):
    print(stack.pop())

from queue import LifoQueue

stack = LifoQueue(maxsize=4)
stack.put('1')
stack.put('2')
stack.put('3')
stack.put('4')


print(stack.full())
print(stack.qsize())
stack.get()
stack.get()
stack.get()
stack.get()
print(stack.empty())

