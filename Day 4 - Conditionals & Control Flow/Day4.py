# Conditional and Control flow

str(True).lower() == "true"
str("true").title() == "True"

# Example 1
str("true")
print("abc".title())

# Example 2
abc = [1,2,3,4,5]
abc_sq = []
for num in abc:
    new_number = num ** 2
    abc_sq.append(new_number)
print(abc_sq)

# Printing even or odd number
is_even = []
is_odd = []
for num in abc_sq:
    if num % 2 == 0:
        print("This is even number")
        is_even.append(num)
    else:
        is_odd.append(num)
print(is_even, is_odd)

is_factor_of_3 =[]
for num in abc_sq:
    if num % 3 == 0:
        is_factor_of_3.append(num)
    elif num % 2 == 0:
        is_even.append(num)
    else:
        is_odd.append(num)

print(is_factor_of_3)

# Control flow with while loops
# Example 3
x = 10
i = 0
while i < x:
    print(i)
    i = i+1
print(i)

# Example 4
while i < x:
    i += 1
    if i % 2 == 0:
        continue
        print(i)
