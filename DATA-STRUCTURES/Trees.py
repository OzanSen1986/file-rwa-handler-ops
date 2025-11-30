'''
Properties of Tree Data Structure:
Number of edges: An edge is the connection between two nodes. 
A tree with N nodes will always have N - 1 edges. 
There is exactly one path from any node to any other node in the tree.
Depth of a node: The depth of a node is the length of the path from the root to that node. 
Each edge in the path adds 1 unit to the length. 
Equivalently, it is the number of edges from the root to the node.
Height of the tree: The height of the tree is the length of the longest path from the root to any leaf node.
Degree of a node: The degree of a node is the number of subtrees attached to it (i.e., the number of children it has).
A leaf node has a degree of 0.
The degree of the tree is the maximum degree among all nodes in the tree.

Binary Search Tree is a tree that allows fast search, insert, delete on a sorted data. 
It also allows finding closest item
'''

import sys

class Node:
    def __init__(self, x: int):
        self.data = x
        self.children = []

def add_child(parent: Node, child: Node):
    parent.children.append(child)

def printParents(node: Node, parent: Node):
    if parent is None:
        print(str(node.data) + " -> NULL")
    else:
        print(str(node.data) + " -> " + str(parent.data))

    for child in node.children:
        printParents(child, node)

def PrintChildren(node: Node):
    children_str = " ".join(str(child.data) for child in node.children)
    print(str(node.data) + " -> " + children_str)
    
    for child in node.children:
        PrintChildren(child)

def PrintLeafNodes(node: Node):
    if not node.children:
        sys.stdout.write(str(node.data) + " ")
        return
    
    for child in node.children:
        PrintLeafNodes(child)

def PrintDegrees(node, parent):
    degree = len(node.children)
    if parent is not None:
        degree +=1
    print(str(node.data) + " -> " + str(degree))

    for child in node.children:
        PrintDegrees(child, node)

def main() -> None:
    
    # creating nodes
    root = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    # constructing tree
    add_child(root, n2)
    add_child(root, n3)
    add_child(n2, n4)
    add_child(n2, n5)


    print('Parents of each node: ')
    printParents(root, None)

    print('Children of each node: ')
    PrintChildren(root)

    print('LeafNodes :')
    PrintLeafNodes(root)
    print('\n')

    print('Degrees of nodes: ')
    PrintDegrees(root, None)


if __name__ == "__main__":
    main()




    








