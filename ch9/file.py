myfile = open('myfile.txt', 'w')
print(myfile.write('hello text file\n'))
myfile.write('goodbye text file\n')
myfile.close()

myfile = open('myfile.txt')
print(myfile.readline())
myfile.readline()
myfile.close()