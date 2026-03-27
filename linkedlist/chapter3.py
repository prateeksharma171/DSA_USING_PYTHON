class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            return

        last=self.head
        while last.next!=self.head:
            last=last.next

        new_node.next=self.head
        last.next=new_node
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            return

        last_node=self.head
        while last_node.next!=self.head:
            last_node=last_node.next
        last_node.next=new_node
        new_node.next=self.head

    def insert_at_middle(self,data,val):
        new_node=Node(data)
        last_node=self.head
        
        while True:
            if(last_node.data==val):
                new_node.next=last_node.next
                last_node.next=new_node
                return
            last_node=last_node.next
            if last_node==self.head:
                print("Value not found")
                return

    def delete(self,data):
        last_node = self.head
        prev_node = None

        if last_node.data == data:
            if last_node.next == self.head:
                self.head = None
                return

            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            self.head = last_node.next
            temp.next = self.head
            return

        prev_node = last_node
        last_node = last_node.next

        while last_node != self.head:
            if last_node.data == data:
                prev_node.next = last_node.next
                return

            prev_node = last_node
            last_node = last_node.next

        print("Value not found")

    def display(self):
        current_node=self.head
        while True:
            print(current_node.data,end=" -> ")
            current_node=current_node.next
            if current_node==self.head:
                break
        print("(back to head)")


if __name__ == "__main__":
    linked_list=LinkedList()
    linked_list.insert_at_beginning(1)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_beginning(3)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)
    linked_list.insert_at_middle(6,2)
    linked_list.delete(6)
    linked_list.display()