class Queue:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return len(self.items)==0
    
    def length(self):
        return len(self.items)
    
    def insert(self, value):
        self.items.append(value)
    
    def delete(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items.pop(0)
    
    def peek(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items[0]

q=Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)
q.delete()
print(f"Initial value of Queue: {q.peek()}")
print(f"Length of Queue: {q.length()}")