i = 0
while i < 9:
    print(i,'',end = '')
    i += 1

print('')

for j in range(9):
    print(j,'',end = '')
    
print('')
    
for row in range(9):
    if (row)%3 == 0:
        print('')
    for col in range(9):
        if (col)%3 == 0 and col != 0:
            print(end = ' ')
        if col == 8:
            print('{},{}'.format(row, col))
        else:
            print('{},{}'.format(row, col), end = ' ')

print('')

row = int(input('Entered row: '))
for col in range(9):
    if (col)%3 == 0 and col != 0:
        print(end = ' ')
    if col == 8:
        print('{},{}'.format(row, col))
    else:
        print('{},{}'.format(row, col), end = ' ')
        
print('')

col = int(input('Entered column: '))
for row in range(9):
    if (row)%3 == 0 and row != 0:
        print(end = ' ')
    if row == 8:
        print('{},{}'.format(row, col))
    else:
        print('{},{}'.format(row, col), end = ' ')

print('')    
for row in range(3):
    for col in range(3):
        if col == 2:
            print('{},{}'.format(row, col))
        else:
            print('{},{}'.format(row, col), end = ' ')