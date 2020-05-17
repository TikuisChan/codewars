def front_back_split(source, front, back):
    if not source or source.next == None:
        raise 'SourceError'
    a = []
    s1 = s2 = source
    while s1:
        a.append(s1)
        s1 = s1.next
    if len(a) == 2:
        front.data = s2.data
        front.next = None
        s2 = s2.next
        back.data = s2.data
    else:
        front.data = s2.data
        front.next = s2.next
        s2 = s2.next
        mid = len(a) // 2
        for i in range(mid - 1):
            source = source.next
            s2 = s2.next
        if len(a) % 2 == 1:
            source = source.next
            s2 = s2.next
        source.next = None
        back.data = s2.data
        back.next = s2.next
