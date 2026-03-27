class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.items=[None]*size
        self.front=self.rear=-1
    
    def isFull(self):
        if((self.rear + 1)% self.size == self.size):
            return True
        return False
    
    def isEmpty(self):
        if(self.front == -1):
            return True
        return False

    def enqueue(self,value):
        if(self.isFull()):
            print("Queue is Full")
            return
        elif(self.isEmpty()):
            self.front = self.rear = 0
            self.items[self.rear]=value
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value
    
    def delete(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        elif(self.front == self.rear):
            self.front = self.rear = -1
        else:
            self.front = (self.front+1)%self.size
    
    def peekAtFront(self):
        print(self.items[self.rear])
    
    def peekAtEnd(self):
        print(self.items[self.front])

queue=CircularQueue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.delete()
queue.delete()
queue.delete()
queue.delete()
queue.enqueue(60)
queue.enqueue(70)
queue.enqueue(80)
queue.enqueue(90)
queue.peekAtEnd()
queue.peekAtFront()
