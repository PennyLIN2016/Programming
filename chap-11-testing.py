'''
11-2//3/4/5

def selectSort(list1):

    loop = 0
    for i in range(len(list1)-1):
        min_index = i
        min_loop = list1[i]
        for j in range(i,len(list1)):
            if list1[j] < min_loop:
                min_loop = list1[j]
                min_index = j
                loop += 1
        if min_index != i:
            list1[min_index] = list1[i]
            list1[i] = min_loop

        #print' The i is %i:'%i,list1
    #print ' the len of the list is %i,The select loop is %i'%(len(list1),loop)

def insertSort(list2):

    i = 1
    loop =0
    for i in range(1,len(list2)):
        j = 0
        while j<i and list2[j] <= list2[i]:
            loop +=1
            j += 1
        if j != i:
            loop_min = list2[i]

            for k in range(i,j,-1):
                list2[k]= list2[k-1]
            list2[j]= loop_min
        #print' The i is %i:'%i,list2
    #print ' the len of the list is %i,The select loop is %i'%(len(list2),loop)

def insertion_sort(list3):
    i = 0
    while i != len(list3):
        insert(list3,i)
        i +=1
        #print' The i is %i:'%i,list3

def insert(list3,pos):
    i = pos
    while i != 0 and list3[i-1] >= list3[pos]:
        i = i-1
    value = list3[pos]
    del list3[pos]
    list3.insert(i,value)

def bubble_sort(L):
    for i in range(len(L)-1,0,-1):
        bubble_pro(L,i)
        #print ' The i is %i:'%i,L

def bubble_pro(L,pos):
    max_pos = pos
    max_value = L[pos]
    for i in range(pos):
        if max_value < L[i]:
            max_pos = i
            max_value = L[i]
    L[max_pos] = L[pos]
    L[pos] = max_value

def bubble_sort_low(L):
    for i in range(0,len(L)-1):
        bubble_pro_low(L,i)
        #print ' The i is %i:'%i,L

def bubble_pro_low(L,pos):
    mix_pos = pos
    mix_value = L[pos]
    for i in range(pos+1,len(L)):
        if mix_value >L[i]:
            mix_pos = i
            mix_value = L[i]
    L[mix_pos] = L[pos]
    L[pos] = mix_value

import time

if __name__ =='__main__':
    list_old = [6,5,4,3,7,1,2,11,56,-1,23,99,104,77,45,65,-3]

    t1 = time.time()
    list3= list_old[:]
    selectSort(list3)
    t2= time.time()
    print'---------------------------------------------------'
    print 'The original list is ',list_old
    print 'the selectSort list is ', list3
    print 'The duration is (s):%f'%((t2-t1)*1000)

    t1 = time.time()
    list4 = list_old[:]
    insertSort(list4)
    t2= time.time()
    print'---------------------------------------------------'
    print 'The original list is ',list_old
    print 'the insetSort list is ', list4
    print 'The duration is (s):%f'%((t2-t1)*1000)

    t1 = time.time()
    list5 = list_old[:]
    insertion_sort(list5)
    t2 = time.time()
    print'---------------------------------------------------'
    print 'The original list is ',list_old
    print 'the insetSort list is ', list5
    print 'The duration is (s):%f'%((t2-t1)*1000)

    t1 = time.time()
    list1= list_old[:]
    bubble_sort(list1)
    t2 = time.time()
    print'---------------------------------------------------'
    print 'The original list is ',list_old
    print 'the bubbleSort list is ', list1
    print 'The duration is (s):%f'%((t2-t1)*1000)

    t1= time.time()
    list2= list_old[:]
    bubble_sort_low(list2)
    t2 = time.time()
    print'---------------------------------------------------'
    print 'The original list is ',list_old
    print 'the bubbleSort_low list is ', list2
    print 'The duration is (s):%f'%((t2-t1)*1000)

'''
'''
11-9
'''
def merge(L1,L2):
    newL = []
    i1 = 0
    i2 = 0

    while i1 <= len(L1) and i2 <= len(L2):
        if i1 < len(L1) and i2 < len(L2) and L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        elif i1 < len(L1) and i2 < len(L2) and L1[i1] >= L2[i2]:
            newL.append(L2[i2])
            i2 += 1
        elif i1 == len(L1):
            newL.extend(L2[i2:])
            i1 += 1
        else:
            newL.extend(L1[i1:])
            i2 += 1
    #newL.extend(L1[i1:])
    #newL.extend(L2[i2:])

    return  newL

def mergesort(L):
    workspalce = []
    for i in range(len(list_old)):
        workspalce.append([list_old[i]])

    i = 0
    while i< len(workspalce)-1:
        L1 = workspalce[i]
        L2 = workspalce[i+1]
        newL = merge(L1,L2)
        workspalce.append(newL)
        i+= 2
        # this is the key of this alg, making sure the merging.

    if len(workspalce)!= 0:
        L[:]= workspalce[-1][:]

if __name__ == '__main__':
    list_old = [6,5,4,3,7,1,2,11,56,-1,23,99,104,77,45,65,-3]

    print 'before Workspace is',list_old
    mergesort(list_old)
    print 'after workspace is ',list_old



