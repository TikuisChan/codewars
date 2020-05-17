class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_duplicates(n):
    if not n or not n.next:
        return n
    head = n
    while n and n.next:
        if n.data == n.next.data:
            n.next = n.next.next
            continue
        n = n.next
    return head
