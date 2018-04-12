import textwrap

#find out every beasts in an input name and come out with the right format
def beasts_in(beasts):
    line = sorted(list(beasts))
    line = ', '.join(line)
    line = 'Beasts in this title: ' + line
    lines = textwrap.wrap(line)
    return lines

#find out the name that has same beasts with the input name
#find out the beasts that appear only in the input name
#return the two lines with right format
def other(t, data):
    all_titles = set()
    beasts = data[t]
    for title in data:
        if title != t:
            if len(data[t] & data[title]) != 0:
                all_titles.add(title)
                beasts = beasts - data[title]
                
    line1 = sorted(list(all_titles))
    line1 = ', '.join(line1)
    line1 = 'Other titles containing beasts in common: ' + line1
    lines1 = textwrap.wrap(line1)
    
    line2 = sorted(list(beasts))
    line2 = ', '.join(line2)
    line2 = 'Beasts appearing only in this title: ' + line2
    lines2 = textwrap.wrap(line2)
    
    return (lines1, lines2)

#store the data of the file 'titles.txt' into a dictionary
data = {}
file = open('titles.txt','r')
for line in file:
    line = line.strip().split('|')
    t = line[0]
    data[t] = set()
    for beast in line[1:]:
        data[t].add(beast)
      
while True:
    
    #input the key word
    title = input('Enter a title (stop to end) => ')
    print(title)
    
    #if the key word is stop, stop looping and stop asking for key word
    if title.lower() == 'stop':
        break
    
    print('')
    found = False
    #find out the first matched name with the key word
    for t in data:
        if title.lower() in t.lower():
            print('Found the following title: {}'.format(t))
            for line in beasts_in(data[t]):
                print(line)
            print('')
            for line in other(t,data)[0]:
                print(line)            
            print('')
            for line in other(t,data)[1]:
                print(line)             
            print('')
            found = True
            break #if find the needed name, input next key word
            
        else:
            continue
    #if can not find the key word in every name, print not found 
    while not found:
        print('This title is not found!')
        break
    
file.close()