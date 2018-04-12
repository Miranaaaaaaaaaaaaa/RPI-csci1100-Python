def bpop_next(bpop,fpop):
    bpop_next = (10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop
    return bpop_next

def fpop_next(bpop,fpop):
    fpop_next = 0.4*fpop + 0.02*fpop*bpop
    return fpop_next

bpop = float(input('Number of bunnies ==> '))
bpop = max(bpop,0)
bpop = round(bpop)
fpop = float(input('Number of foxes ==> '))
fpop = max(fpop,0)
fpop = round(fpop)

bpop_1 = int(bpop_next(bpop,fpop))
fpop_1 = int(fpop_next(bpop,fpop))
bpop_2 = int(bpop_next(bpop_1,fpop_1))
fpop_2 = int(fpop_next(bpop_1,fpop_1))
bpop_3 = int(bpop_next(bpop_2,fpop_2))
fpop_3 = int(fpop_next(bpop_2,fpop_2))
bpop_4 = int(bpop_next(bpop_3,fpop_3))
fpop_4 = int(fpop_next(bpop_3,fpop_3))
'''
bpop_1 = bpop_next(bpop,fpop)
fpop_1 = fpop_next(bpop,fpop)
bpop_2 = bpop_next(bpop_1,fpop_1)
fpop_2 = fpop_next(bpop_1,fpop_1)
bpop_3 = bpop_next(bpop_2,fpop_2)
fpop_3 = fpop_next(bpop_2,fpop_2)
bpop_4 = bpop_next(bpop_3,fpop_3)
fpop_4 = fpop_next(bpop_3,fpop_3)
'''

print('Year 1: {0} {1}'.format(bpop,fpop))
print('Year 2: {0} {1}'.format(bpop_1,fpop_1))
print('Year 3: {0} {1}'.format(bpop_2,fpop_2))
print('Year 4: {0} {1}'.format(bpop_3,fpop_3))
print('Year 5: {0} {1}'.format(bpop_4,fpop_4))
    
