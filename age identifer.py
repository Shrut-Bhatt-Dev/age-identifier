year_birth = int(input("Enter your year of birth (YYYY): "))
age = 2026 - year_birth
print(f"You are {age} years old.")
if age > 26:
    print("You are older than 26.")
else:
    print("You are 26 or younger.")
