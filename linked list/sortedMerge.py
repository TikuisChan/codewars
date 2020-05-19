def sorted_merge(first, second):
    if not first or not second:
        return first if first else second
    if first.data < second.data:
        merge = first
        merge.next = sorted_merge(first.next, second)
    else:
        merge = second
        merge.next = sorted_merge(first, second.next)
    return merge
