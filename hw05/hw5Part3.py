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

# function of one simulation
# return number of turns
def run_one_simulation(grid, prob): 
    
    x = len(grid)//2
    y = len(grid)//2
    turn = 1
    num_false = 3
    num_true = 1    
    
    while True:
        
        # call function move_trainer
        direction, probability = move_trainer()
        
        if direction == 'N':
            x -= 1
        elif direction == 'E':
            y += 1
        elif direction == 'S':
            x += 1
        elif direction == 'W':
            y -= 1
        
        if probability < prob:
            
            t_or_f = throw_pokeball(num_false, num_true)
            if t_or_f == False:
                grid[x][y] -= 1                
                
            elif t_or_f == True:
                grid[x][y] += 1
                num_true += 1
        
        # stop looping if it touch the edge     
        if x <= 0 or x >= (size-1) or y <= 0 or y >= (size-1):        
            break    
                
        turn += 1
        
    return turn
    

size = int(input('Enter the integer grid size => '))
print(size)
prob = input('Enter a probability (0.0 - 1.0) => ')
print(prob)
prob = float(prob)
times = int(input('Enter the number of simulations to run => '))
print(times)
seed_value = 10 * size + size
random.seed(seed_value)    
 
grid = [] 
for i in range(size): 
    grid.append( [0]*size )

# call the function for a given time
i = 1
turns = []
total_turn = 0
while i <= times:   
    turn = run_one_simulation(grid, prob)
    turns.append((turn, i))
    total_turn += turn
    i += 1
turns.sort()

# print out the grid
worst = 0
best = 0
for i in range(size):
    print('')
    for j in range(size):
        best = max(best, grid[i][j])
        worst = min(worst, grid[i][j])
        print('{:5d}'.format(grid[i][j]), end = '')

# print out the statement
print('')
print('Average number of turns in a simulation was {0:.2f}'.format(total_turn/times))
print('Maximum number of turns was {} in simulation {}'.format(turns[-1][0], turns[-1][1]))
print('Minimum number of turns was {} in simulation {}'.format(turns[0][0], turns[0][1]))
print('Best net missed pokemon versus caught pokemon is {}'.format(best))
print('Worst net missed pokemon versus caught pokemon is {}'.format(worst))