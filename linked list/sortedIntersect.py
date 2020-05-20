class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
def sorted_intersect(first, second):
    if not first or not second:
        return None
    inter = i = Node('empty node before head')
    while first and second:
        if first.data != i.data:
            if first.data == second.data:
                i.next = first
                i, first, second = i.next, first.next, second.next
            elif first.data > second.data:
                second = second.next
            else:
                first = first.next
        else:
            first = first.next
    i.next = None
    return inter.next
