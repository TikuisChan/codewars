class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def insert_nth(head, index, data):
    if index < 0:
        raise "Index ValueError"
    if head is None or index == 0:
        return Node(data, head)
    n = head
    ans = n
    while index > 1:
        index -= 1
        n = n.next
    n.next = Node(data, n.next)
    return ans
