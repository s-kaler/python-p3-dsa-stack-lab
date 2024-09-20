class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False

    def push(self, item):
        if not self.full():
            return self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        
    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if self.size() == self.limit:
            return True
        else:
            return False
        

    def search(self, target):
        distance = 0
        for item in reversed(self.items):
            if item == target:
                return distance
            distance += 1
        return -1
