class Stack:
    def __init__(self):
        self.elements = []

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop() 
        else:
            return None

    def is_empty(self):
        return len(self.elements) == 0

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        else:
            return None

class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, value):
        self.elements.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.elements) == 0

    def peek(self):
        if not self.is_empty():
            return self.elements[0]
        else:
            return None

# Create a stack and queue
stack = Stack()
queue = Queue()

# Push values onto the stack and queue
stack.push(1)
stack.push(2)
stack.push(3)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Pop values from the stack and queue
print("Stack pop:", stack.pop())  # Output: 3
print("Queue dequeue:", queue.dequeue())  # Output: 1

# Peek at the top of the stack and queue
print("Stack peek:", stack.peek())  # Output: 2
print("Queue peek:", queue.peek())  # Output: 2
print("Stack first value:", stack.elements[0])  # Output: 1
print("Stack last value:", stack.peek())  # Output: 2

print("Queue first value:", queue.peek())  # Output: 2
print("Queue last value:", queue.peek())  # Output: 2