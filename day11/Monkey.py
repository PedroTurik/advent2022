class Monkey:
    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
    
    def inspect(self):
        item = self.items.pop(0)
        new_item = self.operation(item)//3
        check = self.test(new_item)
        if check:
            return (new_item, self.if_true)
        else:
            return (new_item, self.if_false)
    
    def add(self, item):
        self.items.append(item)
        

class Monkey2:
    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
    
    def inspect(self):
        item = self.items.pop(0)
        new_item = self.operation(item)%(17*19*7*11*13*3*5*2)
        check = self.test(new_item)
        if check:
            return (new_item, self.if_true)
        else:
            return (new_item, self.if_false)
    
    def add(self, item):
        self.items.append(item)