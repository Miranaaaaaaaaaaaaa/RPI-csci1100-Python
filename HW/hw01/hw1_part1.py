r_sun = input("Enter the radius of the Sun (miles) -> ")
print(r_sun)
r_sun = float(r_sun)
r_moon = input("Enter the radius of the Moon (miles) -> ")
print(r_moon)
r_moon = float(r_moon)
d_sun = input("Enter the maximum distance to the Sun (miles) -> ")
print(d_sun)
d_sun = float(d_sun)
d_moon = input("Enter the minimum distance to the Moon (miles) -> ")
print(d_moon)
d_moon = float(d_moon)
rate_moon = input("Enter the rate the Moon is moving away (in/year) -> ")
print(rate_moon)

rate_moon = float(rate_moon)
distance = float(d_sun*(r_moon/r_sun))
recede = float(distance-d_moon)
rate = float((recede*5280*12)/rate_moon)

print('The Moon will have exactly the same apparent size as the Sun when it is {0:.2f} miles away.\nThe Moon will need to recede another {1:.2f} miles\nWhich will occur in {2:.0f} years at the current rate.'.format(distance,recede,rate))