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
