
import webbrowser
import lab05_util

def print_info(name):
    a=name[3].split('+')
    b=sum(name[6])/(len(name[6]))
    print(name[0],'('+name[5]+')')
    print('\t'+a[0])
    print('\t'+a[1])
    print('Average Score: {0:.2f}'.format(b))
    print('')
    return b

restaurants = lab05_util.read_yelp('yelp.txt')
c=int(input('Enter a id=> '))
d=len(restaurants[c-1][-1])


if c-1>len(restaurants) or c-1<=0:
    print('warning')
else:
    m=print_info(restaurants[c-1])
    if 0<m<2:
        print('This restaurant is rated bad, based on {0} reviews.'.format(d))
    elif 2<m<3:
        print('This restaurant is rated average, based on {0} reviews.'.format(d))
    elif 3<m<4:
        print('This restaurant is rated above average, based on {0} reviews.'.format(d))
    elif 4<m<5:
        print('This restaurant is rated very good, based on {0} reviews.'.format(d))
    
    print('What would you like to do next?')
    print('1. Visit the homepage')
    print('2. Show on Google Maps')
    print('3. Show directions to this restaurant')
    e=int(input('Your choice (1-3)? ==>'))
    
    if e==1:
        webbrowser.open(restaurants[c-1][4])
    elif e==2:
        webbrowser.open('http://www.google.com/maps/place/'+restaurants[c-1][3])
    elif e==3:
        webbrowser.open('http://www.google.com/maps/dir/110 8th Street Troy NY/'+restaurants[c-1][3])
    
    
