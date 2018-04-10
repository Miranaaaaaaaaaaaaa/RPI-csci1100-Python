'''import function math'''
import math

'''calculate the volume of the sphere'''
def find_volume_sphere(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

'''calculate the volume of the cube'''
def find_volume_cube(side):
    volume = side ** 3
    return volume

'''input the radius of sphere and the weekly sales'''
radius = input('Enter the gum ball radius (in.) => ')
print(radius)
radius = float(radius)
sales = input('Enter the weekly sales => ')
print(sales)
sales = int(sales)
print('')

'''calculate the required variable'''
target_sales = math.ceil(1.25 * sales)
num_per_edge = math.ceil(math.pow(target_sales, (1/3)))
total_num = math.pow(num_per_edge, 3)
side = num_per_edge * radius * 2
extra_num = int(total_num - target_sales)
wasted_space_target = find_volume_cube(side) - target_sales * (find_volume_sphere(radius))
wasted_space_fill_up = find_volume_cube(side) - total_num * find_volume_sphere(radius)

'''print out the output'''
print('The machine needs to hold {0} gum balls along each edge.'.format(num_per_edge))
print('Total edge length is {0:.2f} inches.'.format(side))
print('Target sales were {0}, but the machine will hold {1} extra gum balls.'.format(target_sales, extra_num))
print('Wasted space is {0:.2f} cubic inches with the target number of gum balls,'.format(wasted_space_target))
print('or {0:.2f} cubic inches if you fill up the machine.'.format(wasted_space_fill_up))