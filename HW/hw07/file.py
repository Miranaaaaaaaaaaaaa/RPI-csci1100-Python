'''
dic_file =  open('words_10percent.txt')

for key in dic_file:
    print(key)
    if key == 'aahed':
        print('FOUND')

int_file = open('input_words.txt')

for key in int_file:
    print(key)
''' 
'''
key_file = open('keyboard.txt')

for key in key_file:
    print(key)
'''

import json
#if __name__ == "__main__": 
movies = json.loads(open("movies.json").read()) 
ratings = json.loads(open("ratings.json").read())

if '3119975' in ratings:
    print('y')

for item in ratings.items():
    print(item)

for item in movies.items():
    print(item)