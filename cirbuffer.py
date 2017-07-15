# Circular buffer
class cirBuffer():
    
    def __init__(self, size):
        self.front = 0
        self.tail = 0
        self.size = size+1
        self.arr = [None]*(self.size)
    
    def isFull(self):
        if (self.front+1)%self.size == self.tail:
            return True
        return False
    
    def isEmpty(self):
        if self.tail == self.front:
            return True
        return False
    
    def insert(self, val):
        if self.isFull():
            raise Exception("Buffer full")
        self.arr[(self.front)%self.size] = val
        self.front = (self.front+1)%self.size
    
    def delete(self, val):
        if self.isEmpty():
            raise Exception("Buffer Empty")
    
        ret = self.arr[self.tail]
        self.tail = (self.tail+1)%self.size
        return ret

        
CB = cirBuffer(5)

for i in range(5):
    CB.insert(i)

for i in range(5):
    print CB.delete(i)
