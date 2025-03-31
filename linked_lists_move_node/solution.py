'''Solution for the Move Node problem from Codewars'''
class Node(object):
    '''Node class'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    '''Context class'''
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''Move a node from the source to the destination'''
    head = source
    source = source.next
    head.next = dest
    dest = head
    return Context(source, dest)
