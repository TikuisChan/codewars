class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if not head or not head.next:
        return head
    temp = head
    h = None
    while temp.next:
        new = Node(temp.data)
        new.next = h
        h, temp = new, temp.next
    head.data = temp.data
    head.next = new
    
