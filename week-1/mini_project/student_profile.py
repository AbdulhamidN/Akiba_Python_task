print("=" * 50)
print("       STUDENT PROFILE SYSTEM")
print("=" * 50)

# to collect student information
fullName = input("Enter your full name: ")
age = int(input("Enter your age: "))
studentID = input("Enter your student ID: ")
city = input("Enter your city: ")
university = input("Enter your university name: ")
department = input("Enter your department: ")
email = input("Enter your email address: ")
phoneNumber = input("Enter your phone number: ")
favoriteLanguage = input("Enter your favorite programming language: ")
programmingGoal = input("Enter your programming goal: ")

#to display student information
print("\n" + "=" * 50)
print("       STUDENT PROFILE")
print("=" * 50)

print(f"Name:              {fullName}")
print(f"student ID:        {studentID}")
print(f"Age:               {age}")
print(f"City:              {city}")
print(f"University:        {university}")
print(f"Department:        {department}")
print(f"Email:             {email}")
print(f"Phone Number:      {phoneNumber}")
print(f"Favorite Language: {favoriteLanguage}")
print(f"Programming Goal:  {programmingGoal}")   

print("=" * 50)
