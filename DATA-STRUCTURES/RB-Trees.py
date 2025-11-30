class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None
    
class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val) -> None:
        new_node = RBNode(val)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return
        # parent is the new node's parent
        new_node.parent = parent
        if parent is None:
            self.root = new_node
            return
        if new_node.val < parent.val:
            parent.left = new_node
            return
        if new_node.val > parent.val:
            parent.right = new_node
            return
        raise Exception('This should never happen')
    
        










            





