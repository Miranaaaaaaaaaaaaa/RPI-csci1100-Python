scores=input('Enter the scores file: ')
print(scores)
sort=input('Enter the output file: ')
print(sort)

first=open(scores)
f=[]
for num in first:
    f.append(int(num))
f.sort()
first.close()

second=open(sort,'w')
for num in range(len(f)):
    second.write('{0:2d}: {1:3d}\n'.format(num,f[num]))
second.close()
