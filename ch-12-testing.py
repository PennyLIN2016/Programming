'''
12-13

def find_min_max(values):

    min = None
    max = None
    for value in values:
        if min == max and max == None:
            max = value
            min = value
        if value> max:
            max= value
        if value < min:
            min =value
    print 'The minimum is ', min
    print 'The maximum is ', max

if __name__ == '__main__':
    list_check = [6, 5, 4, 3, 7, 1, 2, 11, 56, -1, 23, 99, 104, 77, 45, 65, -3]
    find_min_max(list_check)

    list_1 = 'abdfkudahotupl'
    find_min_max(list_1)
'''
'''
12-14

def summmation(limit):
    total = 0
    current = limit
    while current != 0:
        total += current
        current -= 1
    return total
if __name__ == '__main__':
    try:
        print summmation('k')
    except:
        print 'the input is not a number!'
'''





