class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def sorted_insert(head, data):
    if head is None or data < head.data:
        return Node(data, head)
    n = ans = head
    while n and data > n.data:
        n_before = n
        n = n.next
    n_before.next = Node(data, n_before.next)    # or use push(n, data)
    return ans
