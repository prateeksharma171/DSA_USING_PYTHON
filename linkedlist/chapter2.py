class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class doublyLinkedList:
    def __init__(self):
        self.head=None

    def insertAtStart(self,data):
        new_node=Node(data)

        if self.head is not None:
            self.head.prev=new_node

        new_node.next=self.head
        self.head=new_node
    
    def insertAtMid(self,data,loc):
        new_node=Node(data)
        last_node=self.head

        while last_node.next:
            if last_node.data == loc:
                new_node.next=last_node.next
                last_node.next.prev=new_node
                last_node.next=new_node
                new_node.prev=last_node
                return
            last_node=last_node.next


    def insertAtEnd(self,data):
        new_node=Node(data)

        if(self.head == None):
            self.head=new_node
            return
        
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
        new_node.prev=last_node
    
    def delete(self,data):
        last_node=self.head

        if last_node.data == data:
            self.head=last_node.next
            self.head.prev=None
            return

        while last_node.next:
            if last_node.data == data:
                last_node.prev.next=last_node.next
                last_node.next.prev=last_node.prev
                return
            last_node=last_node.next
        
        if last_node.data == data:
            last_node.prev.next = None
            return
    
    def print(self):
        current_node=self.head

        while current_node:
            print(current_node.data, end=" -> ")
            current_node=current_node.next
        print("None")

list = doublyLinkedList()
list.insertAtEnd(1)
list.insertAtEnd(2)
list.insertAtEnd(3)
list.insertAtEnd(4)
list.insertAtEnd(5)
list.insertAtStart(6)
list.insertAtStart(7)
list.insertAtMid(10,3)
list.delete(10)
list.print()