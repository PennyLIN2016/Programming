import sys
def process_file(filename):

    input_file = open(filename,'r')
    for line in input_file:
        line = line.strip()
        print line

    input_file.close()

if __name__ == "__main_":
    process_file(sys.argv[1])

field = ((4,int),(2,int),(2,int),
         (2,int ))

