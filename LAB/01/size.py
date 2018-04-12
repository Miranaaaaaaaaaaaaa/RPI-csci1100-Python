base10size = int(input('Disk size in GB => '))
print(base10size)

base2size = int( base10size * 10**9 / 2**30 )
lostsize = base10size - base2size

print('{} GB in base 10 is actually {} GB in base 2, {} GB less than advertised.'.format(base10size, base2size, lostsize))
print('Input: ', '*'*base10size)
print('Actual:', '*'*base2size)