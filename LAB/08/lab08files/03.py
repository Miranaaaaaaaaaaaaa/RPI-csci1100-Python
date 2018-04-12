def get_words(file):
        description=set()
        words1=file.split('|')
        words2=words1[1].replace(',',' ').replace('.',' ').replace('(','').replace(')','').replace('"','')
        words2=words2.strip().split()
        for w in words2:
                w=w.lower()
                if w.isalpha() and len(w)>=4:                              
                        description.add(w)
                else:
                        pass
        return description

file1='allclubs.txt'
filename = input('Enter file name: ')
file=filename+'.txt'
file=open(file)
file=file.read()
file1=open(file1)
s=[]
for line in file1:
        if len(get_words(file) - get_words(line))!=0 or len(get_words(line) - get_words(file))!=0:      
                both= get_words(file)&get_words(line)
                length=len(both)
                line1=line.split('|')
                s.append((length,line1[0]))

s.sort(reverse=True)
for i in range(5):
        print(s[i])