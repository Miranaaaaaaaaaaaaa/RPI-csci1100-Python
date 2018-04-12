'''
f = [[1,2,3,4],[4,3,2,1],[2,1,4,2],[2,1,4,5]]
i = 0
for a in f:
    for j in range(len(a)):
        if j == len(a)//2:
            print('| ', end = ' ')
        print(a[j], end = ' ')
    if i == len(a)//2-1:
        print('')
        print('---------',end='')
    print('')
    i += 1
'''
primt('a')