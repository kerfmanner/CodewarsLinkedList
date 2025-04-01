'''Swap Node Pairs In Linked List'''
class Node:
    '''A node in a linked list.'''
    def __init__(self, next=None):
        self.next = next

def swap(prev, head):
    '''swap the first three nodes in a linked list'''
    first, second, third = head, head.next, head.next.next

    first.next, second.next = third, first

    if prev:
        prev.next = second

    return first, third

def swap_pairs(head):
    '''swap pairs of nodes in a linked list'''
    if not head or not head.next:
        return head

    prev = None
    start_head = head.next

    while head and head.next:
        prev, head = swap(prev, head)
        
    return start_head
