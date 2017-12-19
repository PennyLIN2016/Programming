'''import math
help(math)
'''

import media
import time

#print help(media)
# show all definition in media

pic = media.load_picture('D:\info\job\python\others\PICT5165.JPG')
media.show(pic)
print('the pic upper-left is 0*0;the lower-right is %i*%i'%(media.get_width(pic),media.get_height(pic)))
crop = media.crop_picture(pic,500,300,1000,550)
# the crop is not a object of pic
media.save_as(pic,'D:\info\job\python\others\PICT5165_2.JPG')
pic_1 = media.load_picture('D:\info\job\python\others\PICT5165_2.JPG')
print('the pic_1 upper-left is 0*0;the lower-right is %i*%i'%(media.get_width(pic),media.get_height(pic)))
media.add_text(pic_1, 100,50,'This is a testing!',media.white)
media.show(pic_1)

time.sleep(3)
media.close(pic_1)
for p in media.get_pixels(pic_1):
    new_blue = int(0.5 * media.get_blue(p))
    new_green = int(0.5 * media.get_green(p))
    # make sure the color value is int
    new_red = 255
    media.set_blue(p, new_blue)
    media.set_green(p, new_green)
    media.set_red(p,new_red)

media.show(pic_1)

time.sleep(10)
media.close(pic)
media.close(pic_1)
