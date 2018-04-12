'''calculate how many happy words is there in a sentence'''
def number_happy(sentence):
    sentence = sentence.lower()
    num = sentence.count('laugh') + sentence.count('happiness') + sentence.count('love') + sentence.count('excellent') + sentence.count('good') + sentence.count('smile')
    return num

'''calculate how many sad words is there in a sentence'''
def number_sad(sentence):
    sentence = sentence.lower()
    num = sentence.count('bad') + sentence.count('sad') + sentence.count('terrible') + sentence.count('horrible') + sentence.count('problem') + sentence.count('hate')
    return num

sentence = input('Enter a sentence => ')
print(sentence)

'''call the functions'''
num_happy = number_happy(sentence)
num_sad = number_sad(sentence)

'''print the output'''
print('Sentiment: '+ num_happy * "+" + num_sad * '-')

'''identify whether the sentence is sad, netural or happy by the number of sad words and happy words'''
if num_happy > num_sad :
    print('This is a happy sentence.')
elif num_happy < num_sad :
    print('This is a sad sentence.')
elif num_happy == num_sad :
    print('This is a neutral sentence.')