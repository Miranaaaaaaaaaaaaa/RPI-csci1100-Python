import random

#function that used to determine the directions and a random value 
def move_trainer():
    print("Directions: ['N', 'E', 'S', 'W']")
    print ("Selected {0}, value {1:.2f}".format(random.choice(['N', 'E', 'S', 'W']), random.random()))
    
# function that used to create a list of true and false
# randomly pcik from the list to determine whether the player successfully catch the pokemon 
def throw_pokeball(num_false, num_true):
    list_temp = []
    for index in range(num_false):
        list_temp.append(False)
    for index in range(num_true):
        list_temp.append(True)
    print('Booleans: {}'.format(list_temp))
    print('Selected {}'.format(random.choice(list_temp)))
    
size = int(input('Enter the integer grid size => '))
print(size)
num_false = int(input('Enter the integer number of Falses => '))
print(num_false)
num_true = int(input('Enter the integer number of Trues => '))
print(num_true)
seed = size * 11
print('Setting seed to {}'.format(seed))
random.seed(seed)

# call move_train five times
i = 0
while True:
    if i == 5:
        break
    else:
        move_trainer()
    i += 1

# call throw_pokeball five times    
j = 0
while True:
    if j == 5:
        break
    else:
        throw_pokeball(num_false, num_true)
    j += 1
    