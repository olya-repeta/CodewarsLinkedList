from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    parts = list_repr.split(" -> ")

    values = parts[:-1]

    head = None
    for value in reversed(values):
        head = Node(int(value), head)

    return head
