#!/usr/bin/python -t

def right_justify(param):
    length = len(param)
    print ' '*(70 - length),param

right_justify('world')

