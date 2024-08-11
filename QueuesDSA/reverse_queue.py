from collections import deque

queue = deque()


def reverse_queue(queue: deque):
    stack = []
    while queue:
        stack.append(queue.pop())
    print(stack)


def reverse_queue2(queue: deque):
    stack = []
    while queue:
        stack.append(queue.popleft())
    print(stack)
    while stack:
        queue.append(stack.pop())
    print(queue)


queue.append(10)
queue.append(20)
queue.append(30)
reverse_queue2(queue)
