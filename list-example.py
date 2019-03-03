metals_file = open('D:\info\job\python\others\metals.txt','r')
'''
The txt can be [['4', '9.012'], ['12', '24.305'], ['20', '20.078'], ['38', '87.62'], ['56', '37.327'], ['88', '226']]
'''
metals_lines = metals_file.readlines()
metals_file.close()

metals_reallist = ['']*len(metals_lines)

for i in xrange(len(metals_lines)):
    metals_reallist[i] = metals_lines[i].split()
print metals_reallist

for value in metals_reallist:
    print value[0],value[1]


number_and_weight = ['']*(len(metals_reallist)*2)
# if the size of list is not sure, append() and pop() can be used here.
for i in xrange(len(metals_reallist)):
    number_and_weight[2*i] = metals_reallist[i][0]
    number_and_weight[2*i+1] = metals_reallist[i][1]
print number_and_weight

def SubReserve_function(values):
    # reverse the order of the sublists in values, not the order of value ,but the order of the list of vlaue[i]
    result = []
    for sublist in values:
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0,i)
    return result

new_list = SubReserve_function(metals_reallist)
print new_list
