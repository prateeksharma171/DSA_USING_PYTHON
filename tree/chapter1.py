class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        print(" " * level * 2 + str(self.data))
        for child in self.children:
            child.print_tree(level + 1)

root = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)
grandchild1 = Node(5)

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
child1.add_child(grandchild1)

root.print_tree()
