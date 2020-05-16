class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def push(head, data):
    return Node(data, head)
  
def build_one_two_three():
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    return chained
