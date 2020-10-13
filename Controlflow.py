# 1.Comparision Operators
'''
print(10 > 3)
print(10 >= 3)
print(10 < 20)
print(10 == 10)
print(10 == "10")
print(10 != 10)
print("bag" > "apple")
print("bag" == "BAG")
print(ord("b"))
print(ord("B"))
'''

# 2.Conditional Statements
'''
temp = 15
if (temp > 30):
    print("its warm")
    print("Drink water")
elif temp > 20:
    print("its nice")
else:
    print("its cold")
print("Done")
'''

# 3.Ternary Operator
'''
age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
'''

# 4.Logical Operators
'''
high_income = True
good_credit = False
student = False
if (high_income or good_credit) and not student:
    print("eligible")
else:
    print("Not eligible")
'''

# 5. Short-circuit Evaluation ----> logical operators are short circuit in python
'''
high_income = True
good_credit = True
student = True
if (high_income or good_credit) and not student:
    print("eligible")
'''

# 6. Chaining Comparision Operators
'''
# lets say age should be between 18 and 65
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("eligible")
print("Done")
'''

# 7. QUIZ
# 8. For Loops
'''
# for number in range(3):
#print("Attempt", number)
#print("Attempt", number + 1, (number + 1) * ".")
# for number in range(1, 4):
#    print("Attempt", number, (number) * ".")
for number in range(1, 10, 2):
    print("Attempt", number, (number) * ".")
'''
# 9. For__Else ----> Instead of repeating like for loop does what if
#  we want to send the o/p immediately after a step
'''
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Attempted 3 times and failed")


successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Attempted 3 times and failed")

'''

# 10.Nested for loops
'''
for x in range(5):
    for y in range(3):
        print(f"({x} , {y})")
'''

# 11.Iterables ---> range, string, lists and custom iterables
'''
print(type(5))
print(type(range(5)))
for x in "python":
    print(x)
for x in [1, 2, 3, 4]:
    print(x)
'''


# 12.While Loops
'''
num = 100
while (num > 0):
    print(num)
    num //= 2
# -----------------------------
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

'''
# 13.Infinite loops
'''
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

'''
# 14.Exercise
count = 0
for num in range(1, 10):
    if (num % 2 != 1):
        count += 1
        print(num)
print(f"we have {count} even numbers")
