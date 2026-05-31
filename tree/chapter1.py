class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
    
    def insert(root, value):
        if(root == None):
            return Node(value)
        if(root.data==value):
            return root
        if(root.data>value):
            root.left=Node.insert(root.left,value)
        else:
            root.right=Node.insert(root.right,value)
        return root
    
    def search(root, value):
        if(root == None):
            return print("value not found",end="\n")
        if(root.data==value):
            return print("value found",end="\n")
        if(root.data>value):
            Node.search(root.left,value)
        else:
            Node.search(root.right,value)
    
    def getSuccessor(root):
        root =root.right
        while(root != None and root.left != None):
            root=root.left
        return root

    def delete(root,value):
        if(root==None):
            return root
        
        if(root.data>value):
            root.left=Node.delete(root.left,value)
        elif(root.data<value):
            root.right=Node.delete(root.right,value)  
        else:
            if(root.left==None):
                return root.right
            elif(root.right==None):
                return root.left
            else:
                successor=Node.getSuccessor(root)
                root.data=successor.data
                root.right=Node.delete(root.right,successor.data)
        return root
    
    def print(root):
        if root is None:return

        Node.print(root.left)
        print(root.data, end=" ")
        Node.print(root.right)


root=None
values=[20,15,30,40,12,18,25,50]
for v in values:
    root=Node.insert(root,v)

""" Node.search(root,18)
Node.search(root,180) """
Node.delete(root,20)

Node.print(root)