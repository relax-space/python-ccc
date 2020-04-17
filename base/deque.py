from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(type(queue))
queue.append("Mack")
queue.append("Jary")
print(queue.popleft())
print(queue.popleft())
print(queue)