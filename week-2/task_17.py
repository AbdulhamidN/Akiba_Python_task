secret_number = 25
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations!")
        print(f"You guessed the number in {attempts} attempts.")
        break

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Too high!")

else:
    print("Game Over!")