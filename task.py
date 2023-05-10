def find_minimum_coins(coins, amount):
    # Sort the coins in descending order
    coins.sort(reverse=True)

    if amount < 0:
        return "Invalid amount"

    # Initialize a list to store the minimum number of coins for each amount
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Zero coins are needed to make an amount of zero

    # Iterate through all amounts from 1 to the given amount
    for i in range(1, amount + 1):
        # Iterate through all available coin denominations
        for coin in coins:
            if coin <= i:
                # Check if using the current coin leads to a smaller number of coins
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
            
    
    # Return the minimum number of coins needed for the given amount
    if min_coins[amount] == float('inf'):
        return -1  # Not possible to make change with the given coins
    else:
        return min_coins[amount]

# Example usage
coins = [1, 5, 7, 9, 11]
amount = 25
result = find_minimum_coins(coins, amount)
print(result)  # Output: 3

coins = [7, 9]
amount = 20
result = find_minimum_coins(coins, amount)
print(result)  # Output: -1

coins = [1, 5, 7, 9, 11]
amount = 0
result = find_minimum_coins(coins, amount)
print(result)  # Output: 0

coins = [1, 5, 7, 9, 11]
amount = -1
result = find_minimum_coins(coins, amount)
print(result)  # Output: Invalid amount


