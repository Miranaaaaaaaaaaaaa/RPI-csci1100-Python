phrase = 'Things you wish you knew as a freshman'
phrase1 = phrase.title()
phrase2 = phrase1.replace(" ","")
hashtag = "#" + phrase2
out_string1 = 'The phrase "{0}"'.format(phrase) 
out_string2 = 'becomes the hashtag "{0}"'.format(hashtag)
print(out_string1)
print(out_string2)

