# function that used to check whether this word is alternative or not
def is_alternating(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    # the word should be at least 8 letters
    if len(word) < 8:
        return False
    # the word should have no numbers
    for index in range(len(word)):
        if word[index] not in letters:
            return False
    # the word should not have two adjacent vowels or two adjacent consonants
    for index in range(len(word)-1):
        if word[index] in consonants and word[index+1] in consonants:
            return False
        if word[index] in vowels and word[index+1] in vowels:
            return False
    # the vowels in this word should not be in decrease order
    for index in range(len(word)-2):
        if word[index] in vowels and word[index] > word[index+2]:
            return False
    return True

# print out whether it is alternative or not
i = 0
while True:
    # input the word
    word = input('Enter a word: ')
    print(word)
    
    # if input nothing, it will stop asking for a word
    if len(word) == 0:
        break
    
    else:        
        # if it alternative
        if is_alternating(word.lower()):
            print("The word '{}' is alternating".format(word))
            print('')
        # if it is not alternative
        else:
            print("The word '{}' is not alternating".format(word))
            print('')
        