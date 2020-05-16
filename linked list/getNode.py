def get_nth(node, index):
    if index < 0:
        raise "Invalid index value"
    current_index = 0
    while node:
        if current_index == index:
          return node
        node = node.next
        current_index += 1
    raise "ValueError"
