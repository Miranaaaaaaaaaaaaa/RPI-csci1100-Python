'''change the hour, minute, second of a day in to second'''
def time_to_seconds (hour, minute, second):
    sec = hour * (60**2) + minute * 60 + second
    return sec

'''calculate the number of years must pass to reach currnt year'''
def calculate_years(sec_input, sec_current, rate):
    yea = round((sec_input - sec_current) / rate)
    return yea

'''call the function'''
sec_current = (time_to_seconds (23, 56, 4))

print('The current length of a day is {0} seconds.'.format(sec_current))

sec_input = int(input('Enter the desired day length in seconds => '))
print(sec_input)
print('')

'''calculate the required variables'''
hour = sec_input // (60 ** 2)
minute = (sec_input - (hour * 60 ** 2)) // 60
second = sec_input - (hour * 60 ** 2) - (minute * 60)
rate = (6 * 60 * 60) / (900000000)

'''print the out put'''
print('{0} seconds is a day length of {1} hours {2} minutes and {3} seconds.'.format(sec_input,hour,minute,second))
print('A day change rate of 6 hours every 900000000 years, ')
print('represents {:.6f} seconds per year.'.format(rate))
print('A day length of {0} hours, {1} minutes and {2} seconds,'.format(hour, minute, second))
print('Would be in year {0}'.format(round(calculate_years(sec_input, sec_current, rate)+2018)))