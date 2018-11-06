class Stack:
    # We define the top of the stack as the last item in the list.
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

class Queue:
    # First in, first out. 
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

# Nodes are used in linked lists.
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
    
    def set_next(self, new_next):
        self.next = new_next
    