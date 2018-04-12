file = input("Enter the name of the IMDB file ==> ").strip()
print(file)
counts = dict()
for line in open(file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1

maxc = max(counts.values())

count = 0
for i in counts:
    if counts[i] == 1:
        count += 1
    if counts[i] == maxc:
        name = i        
namemax = list(counts.keys())[-1]

print('{0} appears most often: {1} times'.format(name,maxc))
print('{0} people appear once'.format(count))