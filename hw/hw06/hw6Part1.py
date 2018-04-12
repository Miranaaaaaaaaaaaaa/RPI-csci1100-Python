#function that used to drop letter one by one from a word and store them into a set
def drop(word):
    drop_set = set()
    for index in range(len(word)):
        new_s = word[0:index] + word[index+1:]
        drop_set.add(new_s)
    return drop_set

#function that used to swap adjacent letters one by one and store them into a set
def swap(word):
    swap_set = set()
    for index in range(len(word)-1):
        new_s = word[0:index] + word[index+1] + word[index] + word[index+2:]
        swap_set.add(new_s)
    return swap_set

#function that used to replace letter one by one with 24 letters and store them into a set
def replace(word):
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z' ]
    replace_set = set()
    for index1 in range(len(word)):
        for index2 in range(len(letters)):
            new_s = word[0:index1] + letters[index2] + word[index1+1:]
            replace_set.add(new_s)
    return replace_set

#input dictionary and filename
dic_file=input('Dictionary file => ')
print(dic_file)
input_file=input('Input file => ')
print(input_file)

#transfer the data of dictionary into a set
d = set()
for word in open(dic_file):
    d.add(word.strip())


for word in open(input_file):
    word = word.strip()    
    temp = set()
    temp.add(word) #transfer every word into a set to compare with the words in dictionary
    
    #if the word is correct
    if len(temp & d) != 0:
        print('{0:15} -> {1:15} :FOUND'.format(word, word))
    
    #if the word is wrong
    else:
        #if the word can be corrected by drop
        if len(drop(word) & d) != 0:
            print('{0:15} -> {1:15} :DROP'.format(word, min(drop(word) & d)))
        #if the word can be corrected by swap
        elif len(swap(word) & d) != 0:
            print('{0:15} -> {1:15} :SWAP'.format(word, min(swap(word) & d)))
        #if the word can be corrected by replace
        elif len(replace(word) & d) != 0:
            print('{0:15} -> {1:15} :REPLACE'.format(word, min(replace(word) & d)))
        #if the word can not be corrected 
        else:
            print('{0:15} -> {1:15} :NO MATCH'.format(word,word))