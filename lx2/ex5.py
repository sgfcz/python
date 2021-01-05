import random
a=[]
c=[]
b=0
while b < 20:
    a.append(random.randint(1,100))
    b+=1
print(a)
for i in a:
    if i <= 100 and i > 90:
        c.append('A')
    elif i <= 90 and i >80:
        c.append('B')
    elif i <= 80:
        c.append('C')
print(c)
