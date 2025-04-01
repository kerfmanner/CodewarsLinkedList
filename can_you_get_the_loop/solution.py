'''This module contains a function to detect the size of a loop in a linked list.'''
def loop_size(node):
    '''Loop detection algorithm to find the size of a loop in a linked list.'''
    fast = node
    slow = node

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break
    else:
        return 0

    start_loop = slow
    moving_part = start_loop
    count = 0

    while True:
        moving_part = moving_part.next
        count += 1
        if moving_part is start_loop:
            break

    return count
