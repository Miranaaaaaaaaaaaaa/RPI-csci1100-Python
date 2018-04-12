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

print_info(restaurants[20])