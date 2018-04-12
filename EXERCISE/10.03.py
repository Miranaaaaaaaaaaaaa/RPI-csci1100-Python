co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, 348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
a=sum(co2_levels)
b=a/len(co2_levels)
c=[]

for n in co2_levels:
    if n>b:
        c.append(n)
        d=len(c)
print('Average: {0:.2f}'.format(b))
print('Num above average:',d)