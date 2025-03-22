# Problem 1:
# 1a:
# The output of this code will print
# 0
# 1
# 2

# 1b:
# The loop will execute 5 times.

# 1c:
# The output of this code will print
# 2
# 3
# 4
# 5

# 1d:
# The output of this code will be
# 10
# 7
# 4
# 1

# 1e:
# In order for a while loop to stop, the loop condition must eventually evaluate to false.


# Problem 2:
# This for loop will print all even numbers between 1 and 50
print("Problem 2:")
for i in range (1, 51):
    if i % 2 == 0:
        print(i)


# Problem 3:
# This while loop will calculate the sum of all numbers from 1 to 100
print("\nProblem 3:")
theSum = 0
num = 1

while num <= 100:
    theSum += num
    num += 1
print(theSum)

# New line printed here in order to add readability to the console output
print()

# Problem 4:
# Grocery store cashier tracks the prices of items being scanned

# Prompts the cashier to enter the price of each item. The program will keep
# accepting inputs until the cashier inputs a negative number, which indicates
# the end of the transation
sumOfItemPrices = 0.0

while True:
    itemPrice = float(input("Enter the price of the item being scanned: "))

    if itemPrice < 0:
        break

    sumOfItemPrices += itemPrice

print(f"\nThe total cost of all items scanned is: ${sumOfItemPrices}")