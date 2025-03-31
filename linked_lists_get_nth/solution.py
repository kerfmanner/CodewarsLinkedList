'''Get Nth node in a linked list'''
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    '''Get the nth node in a linked list'''
    if node is None or not isinstance(index,int) or index < 0:
        raise IndexError
    count = 0
    head = node
    while count <= index and head:
        if count == index:
            return head
        count += 1
        head = head.next
    raise IndexError
