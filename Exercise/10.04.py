a=input('Enter the fraction: ')
print(a)
a=float(a)

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, 348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

c=[]
for i in range(len(co2_levels)):
    b=(a+1)*co2_levels[i]
    c.append(b)

co2_levels = c
    
print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))