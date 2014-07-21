#!/usr/bin/python -t


def find_peak(sublist):
    n = len(sublist)/2
    if n == 0:
        return sublist[n]

    if ((n+1) < len(sublist)) and (sublist[n+1] > sublist[n]):
        return find_peak(sublist[n+1:])
    elif sublist[n-1] > sublist[n]:
        return find_peak(sublist[:n])
    else:
        return sublist[n]
        

def get_input():
    global list
    print "Enter the values:",
    n=raw_input()
    list=n.split()
    for i in range(len(list)):
        list[i] = int(list[i])

get_input()
n=find_peak(list)
print n
"""
while n != EOF:
    list[count]=int(n)
    count+=1
    n=raw_input()

for i in list:
    print i,
"""

