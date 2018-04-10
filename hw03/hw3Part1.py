#Jiaxi Mei
#import the required funcion
import read_names

#function that calculate all the data such as number of the names of the entered rank in a certain year, the number of all the 250 names that in a certain year, and the average of them, and the number of stars it need to print out
def all_data ( counts ):  
    top_counts = counts[rank-1]
    total_counts = sum(counts)
    avg = (top_counts / total_counts) * 100
    star = int(avg * 10)
    return (top_counts, total_counts, avg, star)

#function that calculate the number of stars and the average of the year before or after the entered year
def after_before ( counts, index ):
    top_counts = counts[index]
    total_counts = sum(counts)
    avg = (top_counts / total_counts) * 100
    star = int(avg * 10)
    return (star, avg)

#input the year and rank
year = int(input('Enter a year (1881-2013) => '))
print(year)
rank = int(input('Enter a rank (1-250) => '))
print(rank)

#access the data from the file
f = "top_names_1880_to_2014.txt"
read_names.read_from_file(f)

#if the file read successfilly, pass
#if false, exit
if read_names.read_from_file(f):
    pass
else:
    sys.exit()

# if the year or rank are illegal, print not found
if year < 1881 or year > 2013 or rank < 1 or rank > 250:
    print('{0} is not in the range 1881-2013 or {1} is not in the range 1-250'.format(year, rank))
    
else:
    #print out the information of the female names
    (names_1, counts_1) = read_names.top_in_year(year, 'f')
    top_name_f = names_1[rank-1]
    data_1 = all_data(counts_1)
    print( 'The rank {} most popular female name in {} is {}\n\t{} out of {:d} or {:.2f}%' . format( rank, year, top_name_f, data_1[0] , data_1[1], data_1[2]))
    
    #print out the stars
    print('Histogram for {}'.format(top_name_f))
    (names_0, counts_0) = read_names.top_in_year(year-1, 'f')
    if top_name_f not in names_0:
        print('{}:\t{}\t({:.2f}%)'.format(year-1, '*'*data_0[0], 0))
        #if cannot found the name, assume the number of star is zero
    else:
        index_0 = names_0.index(top_name_f)
        data_0 = after_before(counts_0, index_0)
        print('{}:\t{}\t({:.2f}%)'.format(year-1, '*'*data_0[0], data_0[1]))
        #star of the year before
    print('{}:\t{}\t({:.2f}%)'.format(year, '*'*data_1[3], data_1[2])) 
    #star of the enetered year
    (names_2, counts_2) = read_names.top_in_year(year+1, 'f')
    if top_name_f not in names_2:
        print('{}:\t{}\t({:.2f}%)'.format(year+1, '*'*data_2[0], 0))
        #if cannot found the name, assume the number of star is zero
    else:
        index_2 = names_2.index(top_name_f)
        data_2 = after_before(counts_2, index_2)
        print('{}:\t{}\t({:.2f}%)'.format(year+1, '*'*data_2[0], data_2[1]))
        #star of the year after
        
    print('')
    
    #print out the information of male names
    (names_1, counts_1) = read_names.top_in_year(year, 'm')
    top_name_m = names_1[rank-1]
    data_1 = all_data(counts_1)
    print( 'The rank {} most popular male name in {} is {}\n\t{} out of {:d} or {:.2f}%' . format( rank, year, top_name_m, data_1[0] , data_1[1], data_1[2]))
    
    #print out the stars
    print('Histogram for {}'.format(top_name_m))
    (names_0, counts_0) = read_names.top_in_year(year-1, 'm')
    if top_name_m not in names_0:
        print('{}:\t{}\t({:.2f}%)'.format(year-1, '*'*data_0[0], 0))
        #if cannot found the name, assume the number of star is zero
    else:
        index_0 = names_0.index(top_name_m)
        data_0 = after_before(counts_0, index_0)
        print('{}:\t{}\t({:.2f}%)'.format(year-1, '*'*data_0[0], data_0[1]))
        #star of the year before
    (names_2, counts_2) = read_names.top_in_year(year+1, 'm')
    print('{}:\t{}\t({:.2f}%)'.format(year, '*'*data_1[3], data_1[2]))
    #star of the year entered
    if top_name_m not in names_2:
        print('{}:\t{}\t({:.2f}%)'.format(year+1, '*'*data_2[0], 0))
        #if cannot found the name, assume the number of star is zero
    else:
        index_2 = names_2.index(top_name_m)
        data_2 = after_before(counts_2, index_2)
        print('{}:\t{}\t({:.2f}%)'.format(year+1, '*'*data_2[0], data_2[1]))
        #star of the year after