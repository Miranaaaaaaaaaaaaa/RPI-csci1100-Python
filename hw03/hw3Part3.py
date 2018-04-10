#Jiaxi Mei

#function that change the x and y coordination if the command is n or e or s or w
def move(x, y, direction):
    if direction.lower() == 'n':
        if y-20 <= 0 :
            return (x, 0)
        else:
            return (x, y-20)
    elif direction.lower() == 'e':
        if x+20 >= 150:
            return (150, y)
        else:
            return (x+20, y)
    elif direction.lower() == 's':
        if y+20 < 150 :
            return (x, 150)
        else:
            return (x, y+20)
    elif direction.lower() == 'w':
        if x-20 <= 0:
            return (0, y)
        else:
            return (x-20, y)

#enter the initial information
x = 75
y = 75
power = 10
print('Pikachu at ({}, {}) with power {}'.format(x, y, power))

flag = True
i = 0
all_command = []
while flag:
    #stop looping while flag == false
    if i == 10:
        flag = False
    else:
        i += 1
        command = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
        print(command)
        all_command.append(command)
        #if command is w or e or s or n, change the coordination
        if command.lower() == 'n' or command.lower() == 'e' or command.lower() == 's' or command.lower() == 'w':
            if power == 0:
                print('Pikachu is too tired!')
                print('Pikachu at ({}, {}) with power {}'.format(x, y, power))
            else:
                x = move(x, y, command)[0]
                y = move(x, y, command)[1]
                power = power - 1
                print('Pikachu at ({}, {}) with power {}'.format(x, y, power))
        #if the command is attack, descrease the energy by 5
        elif command.lower() == 'attack':
            if power >= 5:
                #if energy larger or equal than 5, attack successful 
                power = power - 5
                print('Bzzzt, Pikachu zaps its foe!')
                print('Pikachu at ({}, {}) with power {}'.format(x, y, power))
            else:
                #if energy smaller than 5, attack failed
                power = 0
                print("Pffft, It's a dud ...")
                print('Pikachu at ({}, {}) with power {}'.format(x, y, power))
        #if the command is rest, energy change to 10
        elif command.lower() == 'rest':
            power = 10
            print('Pikachu at ({}, {}) with power {}'.format(x, y, power))
        #if the command is something else, decrease the energy by 1
        else:
            if power == 0:
                print('Pikachu is too tired!')
                print('Pikachu at ({}, {}) with power {}'.format(x, y, power))
            else:
                power = power - 1
                print('Pikachu at ({}, {}) with power {}'.format(x, y, power))

print('')  
#print all the commands
print('All commands entered:')
print(all_command)
#print the commands with order
print('All commands sorted:')
print(sorted(all_command))