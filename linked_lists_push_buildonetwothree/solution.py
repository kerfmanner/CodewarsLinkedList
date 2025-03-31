'''Solution for the Linked Lists - Push & BuildOneTwoThree problem on Codewars'''
class Node:
    """Node class"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def push(head, data):
    '''Push a node to the head of a linked list'''
    start = Node(data)
    start.next = head

    return start

def build_one_two_three():
    '''Build a linked list with 1, 2, 3'''
    head = None
    for i in range(3, 0, -1):
        head = push(head, i)
    return head
