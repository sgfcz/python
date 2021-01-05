myfile = open('myfile.txt','w')
myfile.write("Hello file World!")
myfile.close()

print(open('myfile.txt').read())
