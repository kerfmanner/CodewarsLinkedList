class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def remove_next(node):
    '''Remove the next node of the current node'''
    if node.next:
        if node.next.next:
            node.next = node.next.next
        else:
            node.next = None

def remove_duplicates(head):
    '''Remove duplicates from the linked list'''

    start_head = head

    while head:

        current_value = head.data

        while head.next and head.next.data == current_value:
            remove_next(head)

        head = head.next

    return start_head
