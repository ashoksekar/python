#!/usr/bin/python -t
debug=False
print "Enter the n:",
n=int(raw_input())
print n

if (n <= 2):
    print 'Not possible'
    exit(1)
def build_list(l, lst):
    global mat1, n
    x = 0
    flat = ()
    for y in lst:
        flat += y
    while x < len(mat1[l]):
        if (debug):
            print mat1[l][x]
            print flat
        if (mat1[l][x][0] not in flat) and (mat1[l][x][1] not in flat):
            if l-1 >= -n:
                ln = len(lst+[mat1[l][x]])
                ret = build_list(l-1,lst+[mat1[l][x]])
                if len(ret) != ln:
                    lst = ret
                    break
            else:
                lst = lst + [mat1[l][x]]
                break
        x += 1
    return lst

mat1 = []
for i in range(n):
    mat1.append([])
    for j in range(2*n):
        j += 1
        if j+i+2 <= 2*n:
            mat1[i].append((j,j+i+2))

if debug:
    print mat1

lst = build_list(-1,[])
if (debug):
    print lst

if len(lst) != n:
    print 'Not possible'
    exit(1)

ans = []
for x in range(2*n):
    ans.append(0)
for x in range(n):
    if (debug):
        print x, lst[x][0], lst[x][1]
    ans[lst[x][0]-1] = n-x
    ans[lst[x][1]-1] = n-x

print ans

