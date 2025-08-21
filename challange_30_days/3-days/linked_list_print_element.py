"""
elementlarni chunchaki print qilib chiqarib berish kerak
example:
    there are 10 node in linked list
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def print_list(head: Node):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print_list(head)