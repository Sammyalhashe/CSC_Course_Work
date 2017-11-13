"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:
"""

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node



def has_cycle(head):
    if(head == None):
        return True
    prevNode = None
    currNode = head
    nodeData = head.data
    nextNode = head.next
    visited = []
    while(head.next != None):
        if(head in visited and (visited.index(head) != (len(visited)-1))):
            return True
        else:
            visited.append(head)
            head = head.next
    return False




