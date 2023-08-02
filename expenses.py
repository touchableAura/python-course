# expenses = [10.50, 8, 5, 15, 20, 5, 3]

# sum = 0

# for x in expenses:
#     sum = sum + x

# total = sum(expenses)

# sep = '' makes separator (,) not add a space 
# print('you spent $', total, sep = '')

# the range function
# range (0, 7 , 1) (start, stop, step values)
# range (0, 7, 1) returns (0 ,1, 2, 3, 4, 5, 6)
# range (2, 14, 2) returns (2, 4, 6, 8, 10, 12)

total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent $", total, sep='')

