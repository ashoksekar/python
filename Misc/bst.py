#!/usr/bin/python -t

import math
import sys
from get_input import *


class node(object):
    """
    data = number
    parent= parent node
    left = left child
    right = right child
    """
    """ Make sure nodew / 3 = dwidth """
    between_node_width = 6
    node_data_width = 2
    node_avail_list = []
    node_avail_ptr = []
    def __init__ (self, data = 0, parent = None, 
            left = None, right = None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
    def __str__ (self):
        return str(self.data)
    @staticmethod
    def height_from_root(selfie):
        i = 0
        n = selfie
        while n.parent != None:
            i += 1
            n = n.parent
        return i
    @staticmethod
    def length_till_leaves(selfie):
        if selfie == None:
            assert 0
        n = selfie
        while n.parent != None:
            n = n.parent
        x = [0]
        node.length_till_leaves1(n, 0, x)
        return (x[0] - (node.height_from_root(selfie))) 

    @staticmethod
    def length_till_leaves1(selfie, n, length):
        if selfie == None:
            if n > length[0]:
                length[0] = n
            return 
        n += 1
        node.length_till_leaves1(selfie.left, n, length)
        node.length_till_leaves1(selfie.right, n, length)
        return 
    @staticmethod
    def traverse_level_node(selfie, parent, callback, level):
        if selfie == None or node.height_from_root(selfie) == level:
            callback(selfie, parent, level)
            return
        node.traverse_level_node(selfie.left, selfie, callback, level)
        node.traverse_level_node(selfie.right, selfie, callback, level)
        return 
    @staticmethod
    def print_node(selfie, parent, level):
        if selfie == None:
            assert parent != None
            length = node.length_till_leaves(parent)
            length -= 1
            print " " * ((node.between_node_width+node.node_data_width)
                    * (int(math.pow(2,length)/2))),
            sys.stdout.softspace=0
            for i in range(int(math.pow(2, (level -
                node.height_from_root(parent))))/2):
                node.node_avail_list.append(0)
                node.node_avail_ptr.append(parent)
        else:
            length = node.length_till_leaves(selfie)
            hyphen = int(((node.node_data_width + node.between_node_width) *
                          (math.pow(2, (length - 3)))))
            if hyphen < 0 or hyphen < node.between_node_width/2:
                hyphen = 0
            space = (((node.between_node_width) *
                      (int (math.pow(2, (length - 1)))-1)) +
                      ((node.node_data_width) *
                      (int (math.pow(2, (length - 1))+ 2)))) - 2 * hyphen
            if selfie.left != None:
                print '-' * hyphen,
                sys.stdout.softspace=0
            else:
                print ' ' * hyphen,
                sys.stdout.softspace=0
            print '%02d' % selfie.data,
            sys.stdout.softspace=0
            if selfie.right != None:
                print '-' * hyphen,
                sys.stdout.softspace=0
            else:
                print ' ' * hyphen,
                sys.stdout.softspace=0
            """ To remove the trailing space char """
            print " " * space,
            sys.stdout.softspace=0
            node.node_avail_list.append(1)
            node.node_avail_ptr.append(selfie)
        return
    @staticmethod
    def print_tree(selfie):
        length = node.length_till_leaves(selfie)
        i = 0
        while i < length:
            level = length - i 
            if i == (length-1):
                hyphen = 0
                space = 0
            else:
                hyphen = int(((node.node_data_width + node.between_node_width) *
                         (math.pow(2, (level - 3)))))
                space = ((node.node_data_width + node.between_node_width) *
                         int(math.pow(2, (level - 2))))
                space -= (node.between_node_width+node.node_data_width)/2
            if hyphen < 0:
                hyphen = 0
            space -= hyphen
            print ' ' * space,
            sys.stdout.softspace=0
            node.node_avail_list = []
            node.node_avail_ptr = []
            node.traverse_level_node(selfie, None, selfie.print_node, i)
            if len(selfie.node_avail_list) != int(math.pow(2,i)):
                print selfie.node_avail_list
                print '%d %d %d' % (len(selfie.node_avail_list),
                        int(math.pow(2,i)), i),
                assert 0
            print '' 
            sys.stdout.softspace=0
            if i == (length-1):
                return
            """
            print node.node_avail_list
            """
            print ' ' * space,
            sys.stdout.softspace=0
            x = 0
            while x < len(node.node_avail_ptr):
                if node.node_avail_list[x] != 0:
                    if node.node_avail_ptr[x].left != None:
                        print '|' ,
                        sys.stdout.softspace=0
                    else:
                        print ' ' ,
                        sys.stdout.softspace=0
                    print ' ' * (2 * hyphen),
                    sys.stdout.softspace=0
                    if node.node_avail_ptr[x].right != None:
                        print '|', 
                        sys.stdout.softspace=0
                    else:
                        print ' ',
                        sys.stdout.softspace=0
                    print ' ' * (2 * hyphen - node.node_data_width),
                    sys.stdout.softspace=0
                else:
                    y = node.length_till_leaves(node.node_avail_ptr[x])
                    y -= 1
                    print ' ' * ((node.between_node_width +
                        node.node_data_width) * int(math.pow(2,y))/2), 
                    sys.stdout.softspace=0
                    tmp = node.node_avail_ptr[x]
                    while (x < len(node.node_avail_ptr) and
                            node.node_avail_ptr[x] == tmp):
                        x += 1
                    continue
                    sys.stdout.softspace=0
                x += 1
            print '' 
            i += 1
        return
    def __del__(selfie):
        print 'deleted: ', self
    @staticmethod
    def add_node(selfie, new):
        if new.data > selfie.data:
            if selfie.right == None:
                selfie.right = new
                new.parent = selfie
            else:
                node.add_node(selfie.right, new)
        else:
            if selfie.left == None:
                selfie.left = new
                new.parent = selfie
            else:
                node.add_node(selfie.left, new)

list = get_input()
root=node(data = list[0])
for i in range(len(list)):
    if i == 0:
        continue
    new = node(data = list[i])
    node.add_node(root, new)

node.print_tree(root)

