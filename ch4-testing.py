'''import math
print help(math)

print ('1-a :%i'%abs(round(-4.3)))
print ('1-b : %s'%math.ceil(math.sin(34.5)))
'''

'''
import calendar
import datetime

print help(calendar)
#print help(datetime)

flag = 0
cyear = datetime.datetime.now().year
print('The current time is %s . The year is %i'%(datetime.datetime.now(),datetime.datetime.now().year))

while not flag:
    cyear +=1
    if calendar.isleap(cyear):
        flag = 1
        print ('the next leap year is %i'%cyear)


leap_num = calendar.leapdays(2000,2050)
print ('The number of leap years between 2000 and 2050 is %i'%leap_num)

Day_week = calendar.weekday(2016,7,29)
print ('29-7-2016 is %s'%Day_week)
'''
'''
print help(str)
print str.capitalize('boolean')
print ('The first 2 is in pos of %i'%str.find('C02 H20','2'))
print ('The first 2 is in pos of %i'%str.find('C02 H20','2',3))
print  ('boolean starts with lower: %s'%str.islower('Boolean'[0]))
print ('The answer of 3-e is %s'%str.lower('MoNDay').capitalize())
print (' The answer of 3-f is:%s'%str.strip(' Monday'))
'''
import math
print ('%6f'% math.sqrt(8))
print ('\'%6f\''% math.sqrt(8))

