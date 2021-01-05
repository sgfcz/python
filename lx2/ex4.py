L = [1,2,4,8,16,32,64]
X = 5

i = 0

'''while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    else:
        i = i+1
        '''
'''for num in L:
    if 2 ** X == num:
        print(L.index(2 ** X))
    else:
        pass
'''

'''if 2 ** X in L:
    print(L.index(2 ** X))'''

L = []
for i in range(8):
    L.append(2 ** i)
print(L)
    
L = []
L = list(map(lambda x: 2 ** x,range(8)))
print(L)