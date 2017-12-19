'''vel= [0.0,9.81,19.62,29.43]
for speed in vel:
    print "metric:",speed,"m/sec",
    # , not new line for next print in python 2.x
    #print("metric:%.2f m/sec"%speed, end= '' )
    # , not new line for next print in python 3.x
'''

# multiplication Table
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







