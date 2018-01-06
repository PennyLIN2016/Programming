'''
9-1 find_dups: the set and dictionary.

import sys
def find_dups(list_test):
    result = set()
    count_list = {}

    for i in list_test:
        if i in  count_list:
            count_list[i] += 1
        else:
            count_list[i] = 1
    print count_list

    for key in count_list:
        if count_list[key]>= 2 :
            result.add(key)
    ##notice the using of dictionary
    ## the set and the dictionary are both not iterable.
    # the incorrect expression : for (key,value)in count_list:
    # the other correct expression : for (key,value) in count_list.items()

    print result

    return result

if __name__ == '__main__':

    list_count = [4,5,7,10,23,56,4,4,2,1,5,8,56,10,12,12,12]
    print list_count
    find_dups(list_count)
'''
'''
9-2 mating_pairs --set

def mating_pairs(females,males):
    pairs = set()
    if len(females)!= len(males):
        print 'The input data is incorrect!'
        return None
    for i in range(len(females)):
        pairs.add((females.pop(),males.pop()))
    return pairs


if __name__ == '__main__':
    females_set= (['Jane','Rose','Lucy','Ada','Cici'])
    males_set= (['Mike','Joey','herry','Tom','Ben'])
    # Notie: the expression of the values of set, different to the way of tuple
    print 'Before:',females_set,'+',males_set
    print 'The pairs are ',mating_pairs(females_set,males_set)
    print 'after:',females_set,'+',males_set
'''
'''
9-3 
def read_author(name_file):
    name_list = set()
    reading =False
    lines = name_file.readlines()
    for value in lines:
        line_words = value.strip()

        if line_words != '':
            chars = line_words.split()
        else:
            continue

        if not reading:

            if str.lower(chars[0])=='author' and len(chars)> 1 :
                name_list.add(chars[1])
                reading =False
            elif str.lower(chars[0])=='author' and len(chars)== 1:
                reading = True

        else:
            if chars != '':
                name_list.add(chars[0])
                reading = False
    return name_list


if __name__ == '__main__':
    file_list = ['D:\info\job\python\others\Author1.txt','D:\info\job\python\others\Author2.txt','D:\info\job\python\others\Author3.txt']
    name_set_total = set()
       file_current = open(value)
        name_set = read_author(file_current)
        name_set_total = name_set_total | name_set
        file_current.close()
    for value in file_list:
 
    print 'The authors is ',name_set_total
'''
'''
9-5

def find_nounique(name_dic):
    if name_dic == {}:
        return None
    no_unique = set()
    for key,value in name_dic.items():
        if value > 1:
            no_unique.add(key)

    return no_unique


if __name__=='__main__':

    name_map = {'Jane':3,'Rose':1,'Lucy':5,'Ada':1,'Cici':1,
                'Mike':2,'Joey':1,'herry':2,'Tom':1,'Ben':1}
    count_unique = find_nounique(name_map)
    print 'The names are ',name_map
    print 'The number of non unique names is ',len(count_unique),
    print '.The non unique names are ',count_unique
'''
'''
9-6

def find_hardest(dic):
    hardness = -1
    name_hard = ''
    for key,value in dic.items():
        if hardness == -1 or value < hardness:
            hardness = value
            name_hard = key
    return name_hard

if __name__ == '__main__':
    ratio = {'neutron':0.55,'proton':0.21,'meson':0.03,'muon':0.07,'neutrino':0.14}
    name_article = find_hardest(ratio)
    print name_article ,'is the hardest one to be watching.'
'''
'''
9-7 :similar to 9-5
'''
'''
9-8 
def fetch_and_set(dic,key_match,new_value):
    
    for key, value in dic.items():
        if key ==key_match:
            dic[key] = new_value
            return 0
    
        
if __name__ == '__main__':
    
    old_map ={'Jan':1,'Feb':2,'Dec':9}
    key_match = raw_input('Please input the key to match the dic:')
    value = raw_input('please input the new value of the key:')
    print 'The old map : ',old_map
    match_reslut = fetch_and_set(old_map,key_match,int(value))
    print ' The new match :',old_map
    if match_reslut == 1:
        print 'KeyError : the key is not existing in the dic.'
'''
'''
9-10

def match_dic(match1,match2):

    In_dic = {}
    for key, value in match1.items():
        for key1,value1 in match2.items():
            if key==key1 and value==value1:
                In_dic[key]= value
    return In_dic

if __name__ == '__main__':
    match1 = {'Jane':3,'Rose':1,'Lucy':5,'Ada':1,'Cici':1,
                'Mike':2,'Joey':1,'herry':2,'Tom':1,'Ben':1}
    match2 = {'Jane':5,'Rose':1,'Lucy':5,'Ada':7,'Cici':1,
                'Mike':2,'Jon':1,'herry':2,'Tim':1,'Ben':1}
    mew_dic = match_dic(match1,match2)
    print match1
    print match2
    print 'The reslut is ',mew_dic
'''
'''
9-11

def db_headings(dic):
    key_set = set()
    Values = dic.values()
    for i in Values:
        for key in i:
            key_set.add(key)
    return key_set

if __name__ =='__main__':
    dic_Scientist = {
  'jgoodall'  : {'surname'  : 'Goodall',
                 'forename' : 'Jane',
                 'born'     : 1934,
                 'died'     : None,
                 'notes'    : 'primate researcher',
                 'author'   : ['In the Shadow of Man',
                               'The Chimpanzees of Gombe']},
  'rfranklin' : {'surname'  : 'Franklin',
                 'forename' : 'Rosalind',
                 'born'     : 1920,
                 'died'     : 1957,
                 'notes'    : 'contributed to discovery of DNA'},


   'rcarson'  : {'surname'  : 'Carson',
                 'forename' : 'Rachel',
                 'born'     : 1907,
                 'died'     : 1964,
                 'notes'    : 'raised awareness of effects of DDT',
                 'author'   : ['Silent Spring']}
}
    print db_headings(dic_Scientist)
'''
'''
9-12
def db_consistent(dic):
    key_set = []
    Values = dic.values()
    for i in Values:
        key_set.append(set())
        for key in i:
            key_set[-1].add(key)
        print 'the key set is :',key_set[-1]

    if key_set[0]== key_set[1]:
        if key_set[0]==key_set[2]:
            return True

    return  False

if __name__ =='__main__':
    dic_Scientist = {
  'jgoodall'  : {'surname'  : 'Goodall',
                 'forename' : 'Jane',
                 'born'     : 1934,
                 'died'     : None,
                 'notes'    : 'primate researcher',
                 'author'   : ['In the Shadow of Man',
                               'The Chimpanzees of Gombe']},
  'rfranklin' : {'surname'  : 'Franklin',
                 'forename' : 'Rosalind',
                 'born'     : 1920,
                 'died'     : 1957,
                 'notes'    : 'contributed to discovery of DNA'},


   'rcarson'  : {'surname'  : 'Carson',
                 'forename' : 'Rachel',
                 'born'     : 1907,
                 'died'     : 1964,
                 'notes'    : 'raised awareness of effects of DDT',
                 'author'   : ['Silent Spring']}
}
    r = db_consistent(dic_Scientist)
    print 'If items have the same keys? ',r
    
'''
'''
9-14
'''
def sparse_add(v1,v2):
    result_v = v2.copy()
    for key,value in v1.items():
        if key in v2:
            result_v[key] = value + v2[key]
        else:
            result_v[key]= value
    return result_v

def sparse_dot(v1,v2):
    result_v = {}
    for key,value in v1.items():
        if key in v2:
            result_v[key]= value * v2[key]
    return  result_v

if __name__=='__main__':
    vector1 = {0:1,6:3}
    vector2 = {0:2,9:1,5:3}
    print 'v1 is ',vector1
    print 'v2 is ',vector2

    add_v = sparse_add(vector1,vector2)
    print 'The addition is ',add_v

    print 'v1 is ',vector1
    print 'v2 is ',vector2
    dot_v = sparse_dot(vector1,vector2)
    print 'The dot multiplication is ',dot_v




