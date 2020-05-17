class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def append(listA, listB):
    if listA is None:
        return listB
    elif listB is None:
        return listA
    head = listA
    if listA.next:
        while listA.next:
            listA = listA.next
    listA.next = listB
    return head
