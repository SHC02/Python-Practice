# Example 1
my_List = [1, 2, 3, 4, 5]
for my_Var in my_List:
    print(my_Var)
print()

# Example 2
for i in "abc":
    print(i)

print()

# Print b
print("abc"[1])

print()

# Example 3
for x in range(0, 10):
    print(x)

print()

# Example 4
user_1 = {'UserName': 'sehyun123', 'id': 1}
user_2 = {'UserName': 'abc', 'id': 2}
my_Users = [user_1, user_2]
for user in my_Users:
    print(user)
for user in my_Users:
    print(user['UserName'])

# Example 5
user_2 = {'UserName': 'abc', 'id': 2, 'email': 'asd@google.com'}
myUsers = [user_1, user_2]
print(myUsers)
for user in my_Users:
    if 'email' in user:
        print(user['email'])

print()

# Example 6
selected_User = {}
my_User_Lookup = 2
for user in my_Users:
    if 'id' in user and user['id'] == my_User_Lookup:
        selected_User = user
        print(selected_User)

print()

# Example 7
for x in range(0,10):
    for user in my_Users:
        if user['id'] == x:
            print(user)
