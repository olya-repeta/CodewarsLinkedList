class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List must contain at least two nodes.")
    first_head = head
    second_head = head.next
    curr_first = first_head
    curr_second = second_head
    while curr_second and curr_second.next:
        curr_first.next = curr_second.next
        curr_first = curr_first.next
        curr_second.next = curr_first.next
        curr_second = curr_second.next
    curr_first.next = None
    return Context(first_head, second_head)
