# Control Flow in Python
# Control flow is the order in which code is executed.
# It includes conditional statements, loops, and statements like break and continue.
# This helps a program make decisions and repeat actions based on conditions.

# Conditional statements
# Always maintain proper indentation, because Python uses indentation to define blocks.
# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 60:
#     print("You are an adult.")
# else:
#     print("You are a senior.")

# Logical operators
# and: both conditions must be true.
# or: at least one condition must be true.
# not: reverses the condition.
# is_student = True
# has_id = True
#
# if is_student and has_id:
#     print("You are eligible for a student discount.")
# elif is_student or has_id:
#     print("You might be eligible for a partial discount.")
# else:
#     print("You are not eligible for a discount.")

# For loop
# Use a for loop when you know how many times you want to repeat something.
# for i in range(5):
#     print(f"Iteration {i}")

# While loop
# Use a while loop when the loop should continue until a condition becomes false.
# count = 0
# while count < 5:
#     print(f"Count is {count}")
#     count += 1

# break statement
# break stops the loop immediately when a condition is met.
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# continue statement
# continue skips the current value and continues to the next iteration.
for i in range(10):
    if i == 5:
        continue
    print(i)



