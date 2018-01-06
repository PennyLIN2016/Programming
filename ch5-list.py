'''vel= [0.0,9.81,19.62,29.43]
for speed in vel:
    print "metric:",speed,"m/sec",
    # , not new line for next print in python 2.x
    #print("metric:%.2f m/sec"%speed, end= '' )
    # , not new line for next print in python 3.x
'''

# multiplication Table
'''
s = raw_input('The N is :')
print ('Now print out the multiplication table of N!')

N = int(s)
for i in range(1,N+1):
    print '\t'+str(i),
print # the new line

for x in range(1,N+1):
    print str(x),
    for y in range(1,N+1):
        print '\t'+str(x*y),
    print
'''

# read the the specific lines of a file
import sys

def displayLine(file,startline,endline):

    for line in file[startline:endline]:
    # the loop is from startline to endline-1
        print line.strip()

start = raw_input('The start line is :')
end = raw_input('The end line is :')
file = open('d:\info\job\python\others\\tmp.txt','r')
# \\ is for printing '\'
file_txt = file.readlines()
file.close()
# file_txt is a list of lines,not words,
print file_txt

if 0< int(start)<= int(end) and  int(start)<= int(end)<= len(file_txt):
    displayLine(file_txt,int(start)-1,int(end))
else:
    print 'Start is ',start ,', End is ',end,': out of the range of the file(len=',str(len(file_txt)),').'











