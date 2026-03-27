class Dequeue:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return len(self.items)==0
    
    def length(self):
        return len(self.items)
    
    def insertAtEnd(self, value):
        self.items.append(value)
    
    def deleteAtFront(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items.pop(0)
    
    def insertAtFront(self, value):
        self.items.insert(0,value)
    
    def deleteAtEnd(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items.pop()
    
    def peekAtFront(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items[0]
    
    def peekAtEnd(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        return self.items[-1]

q=Dequeue()
q.insertAtEnd(10)
q.insertAtEnd(20)
q.insertAtEnd(30)
q.insertAtEnd(40)
q.deleteAtFront()
print(f"Initial value of Queue: {q.peekAtFront()}")
print(f"Length of Queue: {q.length()}")