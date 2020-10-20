

class Stack(list):
    def __init__(self):
        pass

    def pushstack(self, item):
        self.append(item)

    def popstack(self):
        if(len(self)):
            return self.pop()
        return None

class Queue(list):
    def __init__(self):
        pass

    def pushqueue(self, item):
        self.append(item)

    def popqueue(self):
        if(len(self)):
            return self.pop(0)
        return None

s = Stack()
s.pushstack("hey")
s.pushstack("you")

st = s.popstack()
while st is not None:
    print(st)
    st = s.popstack()

q = Queue()
q.pushqueue("hey")
q.pushqueue("you")

qt = q.popqueue()
while qt is not None:
    print(qt)
    qt = q.popqueue()