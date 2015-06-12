#!/usr/bin/python -t

def get_input():
    str=raw_input("Enter the number")
    list=str.split()
    for i in range(len(list)):
        list[i] = int(list[i])
    print list
    return list

def sort_merge(arr1,arr2):
    print "sort merge: ", arr1, arr2
    arr = []
    arr1len = len(arr1)
    arr2len = len(arr2)
    i = 0
    j = 0
    while i < arr1len:
        while j < arr2len:
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                del arr1[i]
                i -= 1
                arr1len = len(arr1)
                break
            else:
                arr.append(arr2[j])
                del arr2[j]
                j -= 1
                arr2len = len(arr2)
            j += 1
        i += 1
    arr += arr1
    arr += arr2
    print "sorted: ", arr
    return arr

def split_array(array):
    print array
    if len(array) == 1:
        return array
    if (len(array) % 2) != 0:
        index = len(array)/2+1
    else:
        index = len(array)/2
    array1=array[:index]
    array2=array[index:]
    array1=split_array(array1)
    array2=split_array(array2)
    return sort_merge(array1,array2)

print split_array(get_input())
