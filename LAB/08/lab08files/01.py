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

file = input('Enter file name: ')
print('File {} {} words'.format(file,len(get_words(file))))
print(get_words(file))