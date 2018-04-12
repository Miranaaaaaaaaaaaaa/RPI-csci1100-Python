first = input("First => ")
print(first)
second = input("Second => ")
print(second)

str_a = first + '_' + second
low = str_a.lower()
up = str_a.upper()
cap = first.capitalize() + second.capitalize()
underscore = '_' + first + '_' + second
rep_1 = str_a.replace('l','o')
rep_2 = rep_1.replace('o','_')

print('Example variable names')
print('Lower case:', low, len(low))
print('For constants:', up, len(up))
print('Camel case:', cap, len(cap))
print('System variables:', underscore, len(underscore))
print('Silly variable:', rep_2)