class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_sort(list):
    if not list or not list.next:
        return list
    a, b = Node(), Node()
    front_back_split(list, a, b)
    sortList = sorted_merge(merge_sort(a), merge_sort(b))
    return sortList
