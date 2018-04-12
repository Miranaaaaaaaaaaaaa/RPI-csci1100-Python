values = [ 14, 10, 8, 19, 7, 13 ]
v1 = int(input('Enter a value: '))
print(v1)
v2 = int(input('Enter another value: '))
print(v2)
values.append(v1)
values.insert(2, v2)
print(values[3], values[-1])
values.sort()
first = values[len(values)//2-1]
second = values[len(values)//2]
print('Difference: {0}'.format(values[-1]-values[0]))
print('Average: {0}'.format(round(sum(values)/len(values),1)))
print('Median: {0}'.format(round((first+second)/2,1)))