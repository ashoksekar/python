#!/usr/bin/python -t

from get_input import *
from ll import *

list=get_input()
head=tnode=node(data = list[0])
for i in range(len(list)):
    if i == 0:
        continue
    tnode=tnode.add_node_next(node(data = list[i]))

tnode = head
while tnode != None:
    print tnode,
    tnode = tnode.next_node()

print '\nsearching for data...',
print head.search_node(3)
print '\ndeleting node...'
node = head.search_node(3)
node.del_node(node.prev_node(head))
print "%d" % lineno()
del node
print "%d" % lineno()

