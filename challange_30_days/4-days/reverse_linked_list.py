class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)
# [1, 2, 3, 4, 5, 6, 7]
def reverse(head: Node):
    prev = None
    curr = head
    while curr is not None:
        nxt = curr.next # nxt = 2
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print(reverse(head.next.next))


"""arang yechdim zaybal qildiv shu misol ertaga yana tushunishga harakat qilaman"""