c=int(input('Enter a id=> '))

import lab05_util
restaurants = lab05_util.read_yelp('yelp.txt')
i=0
def print_info(name):
    a=name[3].split('+')
    b=sum(name[6])/(len(name[6]))
    print(name[0],'('+name[5]+')')
    print('\t'+a[0])
    print('\t'+a[1])
    print('Average Score: {0:.2f}'.format(b))
    print('')
    return b

m=print_info(restaurants[c-1])
d=len(restaurants[c-1][-1])


if c-1>155 or c-1<0:
    print('warning')
elif 0<m<2:
    print('This restaurant is rated bad, based on {0} reviews.'.format(d))
elif 2<m<3:
    print('This restaurant is rated average, based on {0} reviews.'.format(d))
elif 3<m<4:
    print('This restaurant is rated above average, based on {0} reviews.'.format(d))
elif 4<m<5:
    print('This restaurant is rated very good, based on {0} reviews.'.format(d))