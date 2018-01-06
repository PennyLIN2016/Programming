'''
8-2 : reading the file in a specific and fixed format. the format is defined in fields.

def read_txt(file):
    fields= (
        ((4,int),(2,int),(2,int),),
        ((2,int),(2,int),(2,int)),
        ((2,int),(2,int),(2,int)),
        ((6,float),(6,float),(6,float))
    )
    result = []
    for line in file:
        start = 0
        record = []
        for (width, target_type) in fields:
            text = line[start,width+start]
            value = target_type(text)
            record.append(value)

         result.append(record)
    return result

import sys

input = open('D:\info\job\python\others\\file_width.txt','r')

reslut_1 = read_weather_data(input)

print reslut_1
input.close()
'''
'''
8-3 wrapper the different format to the 8-2

def read_txt(file):
    fields= (
        ((0,int),(4,int),(6,int),),
        ((8,int),(10,int),(12,int)),
        ((14,int),(16,int),(18,int)),
        ((20,float),(26,float),(32,float))
    )
    result = []
    for line in file:
        record = []
        for (width, target_type) in fields:
            if width!= 0:
                text = line[wid_tmp,width-1]
                value = target_type(text)
                record.append(value)
                wid_tmp = width
            else:
                wid_tmp = 0
        text = line[wid_tmp:]
        value = target_type(text)
        record.append(value)

         result.append(record)
    return result

import sys

input = open('D:\info\job\python\others\\file_width.txt','r')

reslut_1 = read_weather_data(input)

print reslut_1
input.close()
'''
'''
8-4 


def smallest_value_skip(reader):

    """ (file open for reading) -> NoneType
    Read and process reader, which must start with a time_series header.
    Return the smallest value after the header.  Skip missing values, which
    are indicated with a hyphen.
    """
    line = reader.readline()
    if line == '':
        pass
        return 'The file is Null'
    smallest = int(line)

    for line in reader:
        line = line.strip()
        if line != '-':
            value = int(line)
            smallest = min(smallest, value)

    return smallest

if __name__ == '__main__':
    with open('D:\info\job\python\others\datanull.txt', 'r') as input_file:
        print(smallest_value_skip(input_file))
'''
'''
8-6
'''
def read_all_molecules(r):
    result = []
    reading = True

    while reading:
        molecule = read_molecule(r)
        if molecule:
            result.append(molecule)
        else:
            reading = False
    return result

def read_molecule(r):
    line = r.readline()
    if not line:
        return None
    if line == '':
        return None
    key,name = line.split()
    if key =='CMNT':
        return None
    molecule = [name]
    reading = True
    old_num = 0
    while reading:
        line = r.readline()
        if line.startswitch("END"):
            reading = False
        else:
            old_num = num
            ke,num,type,x,y,z = line.split()
            if int(old_num) != int(num)+1:
                print line,'The No is incorrect!'
            molecule.append(type,x,y,z)
    return molecule




