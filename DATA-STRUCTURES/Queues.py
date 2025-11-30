'''
queue: stores ordered items, allow items only to be added to the queue, and removed from the head of the queue.

Tail 🔳 -> 🔳 -> 🔳 -> 🔳 -> 🔳 -> 🔳 Head
Enqueue (Push) adds an item to the tail (index-Zero) of the queue.
Dequeue (Pop) removes and returns an item from the head of the queue.
peek returns an item from the head of the queue
'''

class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        if len(self.items) == 0:
            return []
        return len(self.items)
        
q1 = Queue()
q1.push('apple')
q1.push('pear')
q1.push('banana')
q1.pop()
print(q1.items)
# print(q1.peek())














