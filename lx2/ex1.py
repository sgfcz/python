s = 'hello'
m = 0

'''for a in s:
    print(ord(a))
'''

'''for a in s:
    m += ord(a)

print(m)
'''

x = []
for c in s:
    x.append(ord(c))
print(x)
print(list(map(ord,s)))
input()