'''
back a half

import media
import time
pic_1 = media.load_picture('D:\info\job\python\others\PICT5165_2.JPG')

media.show(pic_1)
time.sleep(3)

x, y = media.get_width(pic_1),media.get_height(pic_1)

for j in range(0,y,2):
    for i in range(0,x):
        p = media.get_pixel(pic_1,i,j)
        media.set_color(p,media.black)
# black a line per two lines

media.update(pic_1)
time.sleep(3)
media.close(pic_1)
'''

'''
# copy a pic on to top of the other.
import media
import time

pic_1 = media.load_picture('D:\info\job\python\others\PICT5165.JPG')
w1, h1 = pic_1.get_width(),pic_1.get_height()
print 'The pic 1(background): %i * %i'%(w1,h1)
pic_2 = media.load_picture('D:\info\job\python\others\\ball.JPG')
w2, h2 = pic_2.get_width(),pic_2.get_height()
print 'The pic 2(ball): %i * %i'%(w2,h2)

for x in range(100,919):
    for y in range(200,707):
        p1= pic_1.get_pixel(x,y)
        p2 =pic_2.get_pixel(x-100,y-200)
        media.set_color(p1,p2.get_color())

media.show(pic_1)
time.sleep(3)
media.close(pic_1)
'''



