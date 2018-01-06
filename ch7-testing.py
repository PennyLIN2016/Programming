'''
7-1
def double_preceding(values):
    if values == []:
        pass
    else:
        temp = values[:]
        # temp = values is an alias, temp = values[:] is a copy of slice
        values[0]= 0
        for i in range(1,len(values)):
            values[i]= 2 * temp[i-1]


list_1 = [2,3,5,6,10,121,22]

print list_1
double_preceding(list_1)
print list_1
'''
'''
7-2
rat_1 = [1.0,1.0,1.2,1.5,1.6,1.8,1.8,1.9,2.1,1.9]
rat_2 = [1.3,1.0,1.2,1.9,1.6,2.3,1.8,1.7,2.1,1.8]

if rat_1[0]>rat_2[0]:

    print  'Rat 1 is heavier than rat 2 on the first day!'
    if rat_1[9]>rat_2[9]:
        print 'Rat 1 is heavier than rat 2 all day!'
    else:
        print 'Rat 2 became heavier than rat 1!'
else:
    print 'Rat 1 is lighter than rat 2 on the first day!'
'''

'''
7-4
for i in range(10,0,-1):
    print str(i),'\t',
print 
'''
'''
7-5
sum = 0
for i in range(2,23):
    sum += i
    print 'i is %i sum is %i'%(i,sum)
ave = sum/21
print 'average :%s'%ave
'''
'''7-6
list_1 = [1,2,3,-3,6,-1,-3,1]

def remove_neg(num_list):
    i = 0
    j = 0
    l=len(num_list)
    while i < l:
        if num_list[j] < 0 :
            num_list.remove(num_list[j])
        else:
            j+=1
        i +=1

print list_1
remove_neg(list_1)
print list_1
'''
'''
7-7/8/9
for i in range(7):
    for j in range (i+1):
        print 'T\t',
    print

for i in range(7):
    for j in range(7-i-1):
        print' \t',
    for j in range (i+1):
        print 'T\t',
    print

i= 0
while i<7:
    j = 0
    while j < (7-i-1):
        print ' \t',
        j+= 1

    j = 0
    while j < i+1:
        print'T\t',
        j+= 1
    print
    i+= 1
'''
'''7-10
rat_1_weight = 1.3
rat_2_weight = 1.3
rat_1_rate = 7.00
rat_2_rate = 3.00

rat_1_temp = rat_1_weight
week = 0
while rat_1_temp < rat_1_weight*1.25:
    week += 1
    rat_1_temp = rat_1_temp * (1.00+rat_1_rate/100)
    print 'week: %i weight:%s'%(week,rat_1_temp)
print 'rat_1(25%%) : %i'%week

rat_1_temp = rat_1_weight
rat_2_temp = rat_2_weight
week = 0
while rat_1_temp < rat_2_temp *1.1:
    week +=1
    rat_1_temp = rat_1_temp * (1.00+rat_1_rate/100)
    print 'Rat 1 week: %i weight:%s'%(week,rat_1_temp)
    rat_2_temp = rat_2_temp * (1.00+rat_2_rate/100)
    print 'Rat 2 week: %i weight:%s'%(week,rat_2_temp)
'''
'''7-11 
# Transformation of a pic to left by 90 degrees.
import media
import time

pic_1 = media.load_picture('D:\info\job\python\others\PICT5165_1.JPG')
media.show(pic_1)
time.sleep(2)
media.close(pic_1)

h = media.get_height(pic_1)
w = media.get_width(pic_1)
print 'pic_1: w is %i, h is %i '%(w,h)
pic_2 = media.create_picture(h,w,media.white)
h_2 = media.get_height(pic_2)
w_2 = media.get_width(pic_2)
print 'pic_2: w is %i, h is %i '%(w_2,h_2)
media.show(pic_2)

for x in range(1,w):
    for y in range(1,h):
        p1= media.get_pixel(pic_1,x,y)
        p2 = media.get_pixel(pic_2,(h-y),x)
        # the valid range is 0:h_2-1, 0:w_2-1
        media.set_color(p2,media.get_color(p1))
media.update(pic_2)
media.show(pic_2)
time.sleep(2)
media.show(pic_2)
'''
'''
7-12  reflection of a pic by Y axis


import media
import time

pic_1 = media.load_picture('D:\info\job\python\others\PICT5165_1.JPG')
media.show(pic_1)
time.sleep(2)
media.close(pic_1)

h = media.get_height(pic_1)
w = media.get_width(pic_1)
print 'pic_1: w is %i, h is %i '%(w,h)
pic_2 = media.create_picture(w,h,media.white)
h_2 = media.get_height(pic_2)
w_2 = media.get_width(pic_2)
print 'pic_2: w is %i, h is %i '%(w_2,h_2)
media.show(pic_2)

for x in range(1,w):
    for y in range(0,h):
        p1= media.get_pixel(pic_1,x,y)
        p2 = media.get_pixel(pic_2,w-x,y)
        # the valid range is 0:h_2-1, 0:w_2-1
        media.set_color(p2,media.get_color(p1))
media.update(pic_2)
media.show(pic_2)
time.sleep(2)
media.show(pic_2)
media.close(pic_2)
'''
'''
7-13 downscaling

import media
import time

pic_1 = media.load_picture('D:\info\job\python\others\PICT5165_1.JPG')
media.show(pic_1)
time.sleep(2)
media.close(pic_1)

h = media.get_height(pic_1)
w = media.get_width(pic_1)
print 'pic_1: w is %i, h is %i '%(w,h)
pic_2 = media.create_picture(w/2,h/2,media.white)
h_2 = media.get_height(pic_2)
w_2 = media.get_width(pic_2)
print 'pic_2: w is %i, h is %i '%(w_2,h_2)
media.show(pic_2)

for x in range(0,w_2):
    for y in range(0,h_2):
        p1= media.get_pixel(pic_1,2*x,2*y)
        p2 = media.get_pixel(pic_2,x,y)
        media.set_color(p2,media.get_color(p1))
media.update(pic_2)
media.show(pic_2)
time.sleep(2)
media.close(pic_2)
'''
'''
7-14  Mosaic 

import media
import time

pic_1 = media.load_picture('D:\info\job\python\others\PICT5165.JPG')
media.show(pic_1)
time.sleep(2)
media.close(pic_1)

h = media.get_height(pic_1)
w = media.get_width(pic_1)
print 'pic_1: w is %i, h is %i '%(w,h)

color_w = int(w/10)
color_h = int(h/10)
#color_w = 5
#color_h = 3

color_red = [0]*color_w*color_h
color_green = [0]*color_w*color_h
color_blue = [0]*color_w*color_h

for i in range(color_w):
    for j in range(color_h):
        #print  'BEFORE :i:%i, j:%i, color_red[%i] is %i'%(i,j,(i*3+j),color_red[i*3+j])
        for k in range(10*i,10*(i+1)):
            for m in range(10*j,10*(j+1)):
                p1= media.get_pixel(pic_1,k,m)
                #print 'i:%i, j:%i, k:%i , m:%i'%(i,j,k,m)
                color_red[i*color_h+j] += media.get_red(p1)
                color_green[i*color_h+j] += media.get_green(p1)
                color_blue[i*color_h+j] += media.get_blue(p1)
        color_red[i*color_h+j] = int(color_red[i*color_h+j]/100)
        color_green[i*color_h+j] = int(color_green[i*color_h+j]/100)
        color_blue[i*color_h+j] = int(color_blue[i*color_h+j]/100)

#print color_red
#print color_green
#print color_blue

for x in range(0,w-1):
    for y in range(0,h-1):
        # the size of color list is 1000, index 0-999, so make sure the index less than 1000.
        p1= media.get_pixel(pic_1,x,y)
        #print 'before :i:%i, j:%i, int(x/10)*color_h+int(j/10) is %i'%(x,y,int(x/10)*color_h+int(y/10))
        media.set_blue(p1,color_blue[int(x/10)*color_h+int(y/10)])
        media.set_green(p1,color_green[int(x/10)*color_h+int(y/10)])
        media.set_red(p1,color_red[int(x/10)*color_h+int(y/10)])

media.update(pic_1)
media.show(pic_1)
time.sleep(10)
media.close(pic_1)
'''
'''
7-15 
# Transformation of a pic to a gray one

import media
import time

pic_1 = media.load_picture('D:\info\job\python\others\PICT5165_2.JPG')
media.show(pic_1)
time.sleep(2)
media.close(pic_1)

h = media.get_height(pic_1)
w = media.get_width(pic_1)
print 'pic_1: w is %i, h is %i '%(w,h)

for x in range(0,w):
    for y in range(0,h):
        p1= media.get_pixel(pic_1,x,y)
        p_color = int (media.get_red(p1) +media.get_green(p1)+media.get_blue(p1))/3
        media.set_blue(p1,p_color)
        media.set_green(p1,p_color)
        media.set_red(p1,p_color)

media.update(pic_1)
media.show(pic_1)
time.sleep(10)
media.close(pic_1)
'''
