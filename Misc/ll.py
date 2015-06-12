#!/usr/bin/python -t

class node(object):
    """ data = number
        next = node """
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next
    def __str__ (self):
        return '%d' % self.data
    def __del__(self):
        print "deleted: ", self
    def add_node_next(self, new):
        new.next = self.next
        self.next = new
        return new
    def search_node(self, num):
        node = self
        while node != None:
            if node.data == num:
                return node
            node = node.next
        return node
    def prev_node(self, head):
        node = head
        while node != None and node.next != self:
            node = node.next
        return node
    def del_node(self, prev):
        if prev != None:
            prev.next = self.next
        return self.next
    def next_node(self):
        return self.next

if __name__ == "__main__":
    print node


