#!/usr/bin/python -t
#debug=True
debug=False

def swap(i,j):
    global string
    t = string[i]
    string[i] = string[j]
    string[j] = t

print "Enter the string:",
#GGRBRBBGRBR
string=list(raw_input())
if (debug):
    print string

posr = len(string) + 1
posg = len(string) + 1
posb = len(string) + 1

i = 0
while i < len(string):
    if string[i] == 'R':
        if i > posb:
            swap(i, posb)
            if (posg < len(string)):
                swap(posb, posg)
                posg += 1
            posb += 1
        elif i > posg:
            swap(i, posg)
            posg += 1
        if (posr):
            posr = 0
    elif string[i] == 'G':
        if i > posb:
            swap(i, posb)
            posb += 1
        if (posg > len(string)):
            posg = i
    elif string[i] == 'B':
        if (posb > len(string)):
            posb = i
    i += 1

print "".join(string)
