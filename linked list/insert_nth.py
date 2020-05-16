class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_nth(head, index, data):
    if index < 0:
        raise "Index ValueError"
    if head is None:
        return Node(data)
    current_index = 0
    n = head
    while n:
        if index == 0:
            m = Node(data)
            m.next = n
            return m
        if current_index == 0:
            ans = n
        if current_index == index - 1:
            m = n.next
            n.next = Node(data)
            n = n.next
            n.next = m
            return ans
        current_index += 1
        n = n.next
    raise 'ValueError'
