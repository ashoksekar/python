#!/usr/bin/python -t
debug=False
print "Enter the string:",
string=raw_input()
if (debug):
    print string

d = dict()
i = 0
while i < 128:
    d[chr(i)] = 0
    i += 1
for i in string:
    d[i] += 1
i = 0
res = ''
while i < 128:
    if d[chr(i)] != 0:
        res += chr(i)
        res += str(d[chr(i)])
    i += 1
print res
