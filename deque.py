#0.5초 , 256
# N = 10000
from collections import deque
import sys

class Deque:
    def __init__(self) -> None:
        self.queue =deque()

    def push_back(self, val):
        self.queue.append(val)

    def push_front(self, val):
        self.queue.appendleft(val)

    def front(self):
        if len(self.queue) != 0:
            print(self.queue[0])
        else:
            print(-1)

    def back(self):
        if len(self.queue) != 0:
            print(self.queue[-1])
        else:
            print(-1)

    def empty(self):
        if len(self.queue) != 0:
            print(0)
        else:
            print(1)

    def pop_front(self):
        if len(self.queue) > 0:
            val = self.queue.popleft()
            print(val)
        else:
            print(-1)

    def pop_back(self):
        if len(self.queue) > 0:
            val = self.queue.pop()
            print(val)
        else:
            print(-1)

    def size(self):
        print(len(self.queue))

N = int(input())
q = Deque()
for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    first = cmd[0]
    if len(cmd) > 1:
        val = int(cmd[1])

    if first == 'push_front':
        q.push_front(val)
    elif first == 'push_back':
        q.push_back(val)
    elif first == 'pop_front':
        q.pop_front()
    elif first == 'pop_back':
        q.pop_back()
    elif first == 'front':
        q.front()
    elif first == 'back':
        q.back()
    elif first == 'size':
        q.size()
    elif first == 'empty':
        q.empty()
    else:
        break
        
    
