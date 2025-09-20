age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ").lower()

if age < 13:
    price = 5
elif age <= 17:
    price = 7
else:
    price = 10

# Apply discount for students 13+
if age >= 13 and student == "yes":
    price *= 0.8  # 20% discount

print(f"Your ticket price is: ${price:.2f}")


age = int(input("Enter your age:"))
student = input("Are you a student? (yes/no):").lower()

if age < 13:
    price = 5
elif age <= 17:
    price =  7
else:
    price = 10

# Apply discount for students 13+
if age >= 13 and student == "yes":
    price *= 0.8 # 20% discount

print (f"Your ticket price is: ${price:2f}") 
    
