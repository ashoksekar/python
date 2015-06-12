import inspect

def lineno():
    return inspect.currentframe().f_back.f_lineno

def get_input():
    print "Enter the values:",
    n=raw_input()
    list=n.split()
    for i in range(len(list)):
        list[i] = int(list[i])
    return list
