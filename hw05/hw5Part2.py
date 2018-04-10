import random

#function that used to determine the directions and a random probability
def move_trainer():
    direction = random.choice(['N', 'E', 'S', 'W'])
    probability = random.random()
    return (direction, probability)

# function that used to create a list of true and false
# randomly pcik from the list to determine whether the player successfully catch the pokemon 
def throw_pokeball(num_false, num_true):
    list_temp = []
    for index in range(num_false):
        list_temp.append(False)
    for index in range(num_true):
        list_temp.append(True)
    t_or_f = random.choice(list_temp)
    return t_or_f

size = int(input('Enter the integer grid size => '))
print(size)
p = input('Enter a probability (0.0 - 1.0) => ')
print(p)
p = float(p)
seed_value = 10 * size + size
random.seed(seed_value)

x = size//2
y = size//2
turn = 1
num_poke = 0
num_cap = 0
num_false = 3
num_true = 1

while True:
    
    # the condition that stop lopoping and printing
    if p <= 0 or p >= 1 or  x <= 0 or x >= (size-1) or y <= 0 or y >= (size-1):
        print('Trainer left the field at turn {}, location ({}, {}).'.format(turn-1, x, y))
        print('{} pokemon were seen, {} of which were captured.'.format(num_poke, num_cap))   
        break
    
    # call function move_trainer()
    direction, probability = move_trainer()
    
    if direction == 'N':
        x -= 1
    elif direction == 'E':
        y += 1
    elif direction == 'S':
        x += 1
    elif direction == 'W':
        y -= 1
    
    # if saw a pokemon
    if probability < p:
        print('Saw a pokemon at turn {}, location ({}, {})'.format(turn, x, y))
        num_poke += 1
        
        # call function throw_pokeball
        t_or_f = throw_pokeball(num_false, num_true)
        
        # if catch
        if t_or_f == False:
            print('Missed ...')
        # if not catch
        elif t_or_f == True:
            print('Caught it!')
            num_cap += 1
            num_true += 1
        
    turn += 1    