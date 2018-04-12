def get_words(file):
        description=set()
        for line in open(file):
                words1=line.split('|')
                words2=words1[1].replace(',',' ').replace('.',' ').replace('(','').replace(')','').replace('"','')
                words2=words2.strip().split()
                for w in words2:
                        w=w.lower()
                        if w.isalpha() and len(w)>=4:                              
                                description.add(w)
                        else:
                                pass
        return description

filename1 = input('Enter file name: ')
file1=filename1+'.txt'
filename2 = input('Enter file name: ')
file2=filename2+'.txt'

print('Comparing clubs wrpi and csa:')
print('Same words: {}'.format(get_words(file1)&get_words(file2)))
print('Unique to {}: {}'.format(filename1,get_words(file1) - get_words(file2)))
print('{} {} words'.format(filename1, len(get_words(file1))))
print('Unique to {}: {}'.format(filename2,get_words(file2) - get_words(file1)))
print('{} {} words'.format(filename2, len(get_words(file2))))