menu = ['pizza', 'burger', 'pancakes', 'pasta']   # List of items on the menu
stock = {'pizza' : 3, 'burger' : 4, 'pancakes' : 5, 'pasta' : 1}   # Dictionary of how many of each item we have
price = {'pizza' : 20, 'burger' : 10, 'pancakes': 8.50, 'pasta' : 12}   # Dictionary of how much each item costs

total_stock = 0   # We will add to this using a for loop for each item

for keys in stock:   # For loop to iterate through every key in the stock dictionary
    item_value = (stock[keys] * price[keys])   # Multiplys each item in stocks value by the corresponding item in prices value
    total_stock += item_value   # Adds each individual item_value to the total_stock each time the loop runs
    
print('The total value of your stock is £' + str(total_stock))


