"""Solution"""


class Node:
    """Node class"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    """Returns a string representation of the list"""
    if node is None:
        return "None"

    result = []
    current_node = node

    while current_node:
        result.append(str(current_node.data))
        current_node = current_node.next

    return " -> ".join(result) + " -> None"
