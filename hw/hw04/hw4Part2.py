import math
import hw4_util

# function that used to find all the zip code in one city
def zip_by_location(info_all, location):
    code_list = []
    for line in info_all:
        if line[3].lower() == location[0] and line[4].lower() == location[1]:
            code_list.append(line[0])
    return code_list

# function that used to find the associate information of a zip code
def location_by_zip(info_all, code):
    for line in info_all:
        if line[0] == code:
            return (line[1],line[2],line[3],line[4],line[5])
    return False

# function that used to change the fractional degree to degree, minute, second
def fraction_to_degree(data):
    if data == 0:
        direction = ''
        degree = 0
        minutes = 0
        seconds = 0
    else:
        num = abs(data)
        degree = int(num)
        minutes = int((num - int(num)) * 60)
        seconds = ((num - int(num)) * 60 - minutes) * 60
        if num == data:
            direction = ('N', 'E')
        else:
            direction = ('S', 'W')
    return (degree, minutes, seconds, direction)

# function that used to find the distance between two location
def distance(latitude1, longtitude1, latitude2, longtitude2):
    R = 3959.191
    latitude1 = (latitude1/180)*math.pi
    longtitude1 = (longtitude1/180)*math.pi
    latitude2 = (latitude2/180)*math.pi
    longtitude2 = (longtitude2/180)*math.pi
    la = abs(latitude2 - latitude1) 
    lo = abs(longtitude2 - longtitude1)
    a = (math.sin(la/2))**2 + math.cos(latitude1)*math.cos(latitude2)*(math.sin(lo/2))**2
    d = 2*R*math.asin(math.sqrt(a))
    return d

# read out the information in one zip
info_all = hw4_util.read_zip_all()

while True:
    command = input("Command ('loc', 'zip', 'dist', 'end') => ")
    print(command)
    command = command.lower()
    
    # if the command is end, jump out if the loop
    if command == 'end':
        print('')
        print('Done')
        break
    
    # if the command is loc
    elif command == 'loc':
        code = input('Enter a ZIP code to lookup => ')
        print(code)
        data = location_by_zip(info_all, code)
        # if the entered zip code is invalid
        if data == False:
            print('Invalid or unknown ZIP code')
        else:
            latitude = fraction_to_degree(data[0])
            longtitude = fraction_to_degree(data[1])
            print('ZIP code {0} is in {1}, {2}, {3} county,\n\tcoordinates: ({4:03d}\xb0{5:02d}\'{6:.2f}\"{7},{8:03d}\xb0{9:02d}\'{10:.2f}\"{11})'.format(code, data[2], data[3], data[4], latitude[0], latitude[1], latitude[2], latitude[3][0], longtitude[0], longtitude[1], longtitude[2], longtitude[3][1]))
        print('')
    
    # if the command is dist       
    elif command == 'dist':
        code_1 = input('Enter the first ZIP code => ')
        print(code_1)
        code_2 = input('Enter the second ZIP code => ')
        print(code_2)
        data1 = location_by_zip(info_all, code_1)
        data2 = location_by_zip(info_all, code_2)
        # if the entered zip code is invalid
        if data1 == False or data2 == False:
            print('The distance between {0} and {1} cannot be determined'.format(code_1,code_2))
        # if the entered zip code is valid
        else:
            latitude1 = data1[0]
            longtitude1 = data1[1]
            latitude2 = data2[0]
            longtitude2 = data2[1]
            distance = distance(latitude1, longtitude1, latitude2, longtitude2)
            print('The distance between {0} and {1} is {2:.2f} miles'.format(code_1, code_2, distance))
        print('')
    
    # if the command is zip  
    elif command == 'zip':
        city = input('Enter a city name to lookup => ')
        print(city)
        state = input('Enter the state name to lookup => ')
        print(state)
        location = (city.lower(), state.lower())
        code_list = zip_by_location(info_all, location)
        # if the cit or state is invalid
        if len(code_list) == 0:
            print('No ZIP code found for {0}, {1}'.format(city,state))
        # if they are valid
        else:
            data_zip = location_by_zip(info_all, code_list[0])
            c = ''
            for num in range(len(code_list)-1):
                c += code_list[num] + ', '
            c += code_list[-1]
            print('The following ZIP code(s) found for {0}, {1}: {2}'.format(data_zip[2],data_zip[3],c))
        print('')
    
    # if the command is something else        
    else:
        print('Invalid command, ignoring')
        print('')