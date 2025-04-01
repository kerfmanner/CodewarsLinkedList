'''Alternating Split'''
class Node(object):
    '''Node class for a singly linked list.'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    '''Context class to hold the two split linked lists.'''
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    '''Splits a linked list into two lists, alternating nodes between them.'''
    if head is None or head.next is None:
        raise ValueError

    first_head = head
    second_head = head.next
    head = head.next.next

    first = first_head
    second = second_head
    first_turn = True

    while head:

        if first_turn:
            first.next = head
            first = first.next
        else:
            second.next = head
            second = second.next

        first_turn = not first_turn
        head = head.next

    first.next = None
    second.next = None

    return Context(first_head, second_head)
