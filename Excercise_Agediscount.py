Age = float(input("Enter your age:"))
print(Age)
Student = input("Are you a student? (yes/no):")
if Age <= 12:
    print("You are eligible for a discount on the movie ticket.")
elif 12 < Age < 18:
    print("You are eligible for a discount on the movie ticket.")
else:
    print("You are not eligible for a discount on the movie ticket.")