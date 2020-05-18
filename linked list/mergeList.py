
""" For your information:
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
"""

def shuffle_merge(first, second):
    if not first:
        return second
    elif not second:
        return first
    a, b = first, second
    head = merge = Node(a.data)
    head.next = merge.next = shuffle_merge(b, a.next)
    return head
