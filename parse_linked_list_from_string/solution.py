'''Parse a linked list from a string'''
class Node:
    """Node class"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    '''Convert a string to a linked list'''
    if s == 'None':
        return None

    data = s.split(' -> ')
    head = None

    for i in data:

        if i == 'None':
            continue

        if head is None:
            head = Node(int(i))
            node = head
        else:
            node.next = Node(int(i))
            node = node.next

    return head
