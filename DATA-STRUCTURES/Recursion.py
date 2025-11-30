# fibonacci number
# F(N) --> if N == 0, F(0) = 0
# F(N) --> elif N ==1, F(1) = 1
# F(N) --> else F(N) = F(N-1) + F(N-2)


# Time O(2 ^n)
# Space O(n)

def F(n) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)
    
#print(F(10))


# Linked lists are recursive

class SinglyNode:
    def __init__(self, val, next= None):
        self.val = val
        self.next = next
    def str(self):
        return str(self.val)


Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)
D = SinglyNode(9)

Head.next = A
A.next = B
B.next = C
C.next = D


def reverse(node:SinglyNode):
    if not node:
        return
    
    reverse(node.next)
    print(node.val)

reverse(Head)




