list_1 = [('Beryllium',4),('Magnesium',12),('Calcium',20),
          ('Strontium',38),('Barium',56),('Radium',88)]

alkaline_earth_metals = list_1
'''
5-2
for i in xrange (0,len(alkaline_earth_metals)):
    print 'alkaline_earth_metals[',str(i),'] is ',alkaline_earth_metals[i]
    if alkaline_earth_metals[i][0]== 'Radium':
        print 'The index of "Radium" is ',str(i)


for j in xrange (1,(len(alkaline_earth_metals)+1)):
        print  'alkaline_earth_metals[-',str(j),'] is ',alkaline_earth_metals[-j]
        if alkaline_earth_metals[-j][0]== 'Beryllium':
            print 'The reverse index of "Beryllium" is ',str(-j)
5-2
'''

'''
5-4
max_number = 0

for x in alkaline_earth_metals:
    if x[1] > max_number:
        max_number = x[1]

print 'The Max of the number is ',str(max_number)
5-4
'''
'''
5-6/7
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']

for value in celegans_phenotypes:
    print value

for value in celegans_phenotypes:
    print value,
print
5-6/7
'''

'''
5-8
country_populations = [1295,23,3,47]

total_1 = sum(country_populations)
print 'The sum population is',str(total_1),'millions'

total_2 = 0
for value in country_populations:
    total_2 = total_2 + value
print 'The sum population is',str(total_2),'millions'
'''
'''
5-9/10/11/12/13

temp_list = [25.2,16.8,31.4,23.9,28,22.5,19.6]
temp_list.sort()
print 'The list is now in ascending order: ',temp_list

i= 0
while temp_list[i]< 20:
    i= i+1
cool_temps = temp_list[:i]
warm_temps = temp_list[i:]
print 'The cool_temps is ',cool_temps
print 'The warm_temps is ',warm_temps

temps_in_celsius = cool_temps + warm_temps
print 'The temps_in_celsius is ',temps_in_celsius

temps_in_Fa =[0]*len(temps_in_celsius)
# temps_in_Fa can not be null list. otherwise there will be syntax error in for loop
for j in xrange(0,len(temps_in_celsius)):
    temps_in_Fa[j]= temps_in_celsius[j]*1.8 + 32
    print 'temps_in_Fa[',str(j),']= ',temps_in_Fa[j]

print 'temps_in_Fa',temps_in_Fa
print 'temps_in_celsius',temps_in_celsius
'''
'''
5-14/15/16/17,19
'''
metals_file = open('D:\info\job\python\others\metals.txt','r')
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



