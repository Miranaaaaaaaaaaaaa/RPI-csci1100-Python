
file=input('Data file name: ').strip()
print(file)
prefix=input('Prefix: ').strip()
print(prefix)

s1=set()
name_last=set()
for line in open(file,encoding='ISO-8859-1'):
    w=line.strip().split('|')
    s1.add(w[0].strip())
for n in s1:
    w=n.split(',')
    name_last.add(w[0].strip())

num=[]
for item in name_last:
    if item[0:len(prefix)]==prefix:
        num.append(item)

print('{0} last names'.format(len(name_last)))
print('{0} start with {1}'.format(len(num),prefix))
'''
imdb_file = input("Enter the name of the IMDB file ==> ").strip()

print(imdb_file)

counts = dict()

for line in open(imdb_file, encoding = "ISO-8859-1"):

    words = line.strip().split('|')

    name = words[0].strip()

    if name in counts:

        counts[name] += 1

    else:

        counts[name] = 1

m = sorted(counts.values())[-1]

count = 0

for i in counts:

    if counts[i] == m:

        m = i

    if counts[i] == 1:

        count += 1

print('{} appears most often: {} times'.format(m,counts[m]))

print('{} people appear once'.format(count))
'''