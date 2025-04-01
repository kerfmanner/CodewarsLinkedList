'''sorted_insert'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    '''Insert a node in a sorted linked list'''
    if head is None:
        return Node(data)

    heading = head
    prev = None

    while heading:
        if prev is None:
            if heading.data > data:
                node = Node(data)
                node.next = head
                return node
        else:
            if heading.data > data:
                node = Node(data)
                node.next = heading
                prev.next = node
                return head

        prev = heading
        heading = heading.next

    prev.next = Node(data)

    return head

            