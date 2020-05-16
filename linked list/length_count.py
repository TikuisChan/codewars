class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    i = 0
    while node:
        i += 1
        node = node.next
    return i
    # Your code goes here.
  
def count(node, data):
    i = 0
    while node:
        if node.data == data:
            i += 1
        node = node.next
    return i
