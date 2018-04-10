#Jiaxi Mei
#import the required funcion
import hw3_util

#calculate the required coins that used to change
def can_or_cannot(current, coins, i, final_list):
    if i < 0 or current == 0:
        return final_list
    if current >= coins[i]:
        current = current - coins[i]
        final_list.append(coins[i])
        return can_or_cannot(current, coins, i-1, final_list)
    else:
        return can_or_cannot(current, coins, i-1, final_list)

#input the file's name and the cost in cents
file_name = input('Enter the coin file name => ')
print(file_name)
cost = int(input('Enter the item cost in cents (0-100) => '))
print(cost)
coins = hw3_util.read_change(file_name)   

print('')
print('I have the following coins:')
print(coins)

#state the required information for the function
current = int(100 - cost)
coins.append(current)
coins.sort()
index = coins.index(current)
index = index - 1
final_list = []
print('Change from ${:.2f} is {} cents'.format(1, current))

#call the function
final_list = can_or_cannot(current, coins, index, final_list)

#if cannot change, print how many cents additionaly required to change
if int(sum(final_list)) != current :
    print('I cannot make change with my current coins.')
    print('I need an additional {0} cents.'.format(current-sum(final_list)))
#if can change, print out the number for each kind of coins required
else :
    half_dollars = final_list.count(50)
    quarters = final_list.count(25)
    dimes = final_list.count(10)
    nickels = final_list.count(5)
    pennies = final_list.count(1)
    print('{} Half Dollars, {} Quarters, {} Dimes, {} Nickels, {} Pennies'.format(half_dollars, quarters, dimes, nickels, pennies))