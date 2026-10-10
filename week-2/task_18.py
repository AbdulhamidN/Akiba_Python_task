n = int(input("Enter a positive number: "))

even_count = 0
odd_count = 0
total_sum = 0

for i in range(1, n + 1):
    # Calculate the sum of every number
    total_sum += i

    # Count even and odd numbers
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Sum:", total_sum)