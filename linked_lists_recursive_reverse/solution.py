class Node(object):
    '''node class'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    '''Recursively reverses a linked list.'''
    if head is None or head.next is None:
        return head

    new_head = reverse(head.next)

    head.next.next = head
    head.next = None

    return new_head
