'''
10-1 : revserse a string

def complement(sequence):
    result = ''
    # if using [], the result is a list in [,,,,,] ,not a string like '.....'
    for char in sequence:
        if char == 'A':
            result += 'T'
        elif char =='T':
            result += 'A'
        elif char == 'G':
            result += 'C'
        elif char == 'C':
            result += 'G'
        else:
            result = 'The input DNA is incorrect, including '+ char
            return result
    return  result



if __name__=='__main__':
    orig_dna = 'AATTGCCGT'
    reverse_dna = complement(orig_dna)
    print 'The original DNA is ',orig_dna
    print 'The reverse DNA is  ',str(reverse_dna)
'''

'''
10-2: find out the max or min 

def get_list_number(str_input):
    result_list = []
    str_doing = str_input.split()
    for char in str_doing:
         result_list.append(int(char))
    # herein there should be a error handing for non-num input
    return result_list

def min_or_max_index(num_list,bool):
    tmp = num_list[0]
    tmp_pos = 0
    for i in range (1,len(num_list)):
        if bool:
            if num_list[i] < tmp:
                tmp = num_list[i]
                tmp_pos = i
        else:
            if num_list[i] > tmp:
                tmp = num_list[i]
                tmp_pos = i
    return (tmp,tmp_pos)


if __name__ == '__main__':

    num_input = raw_input('please input the number list:')
    num_list = get_list_number(num_input)
    if num_list != []:
        print 'Before the num_list is ',num_list
        result_get = min_or_max_index(num_list,False)
        print 'The max number and its index is ',result_get
        result_get = min_or_max_index(num_list,True)
        print 'The min number and its index is ',result_get
    else:
        print ' The input is incorrect:',num_input
'''

