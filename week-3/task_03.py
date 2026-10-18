
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def get_divisors(number):
    divisors = []

    if number == 0:
        return divisors

    number = abs(number)

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    return divisors


def sum_of_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10

    return total


def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return reversed_number * sign


def analyze_number(number):
    print("\n===== NUMBER ANALYSIS =====")
    print("Number:", number)

    if number == 0:
        print("Even or Odd: Zero is even")
    elif number % 2 == 0:
        print("Even or Odd: Even")
    else:
        print("Even or Odd: Odd")

    print("Is Prime:", is_prime(number))
    print("Sum of Digits:", sum_of_digits(number))
    print("Reversed Number:", reverse_number(number))
    print("Divisors:", get_divisors(number))

    print("===========================")


number = int(input("Enter an integer: "))

analyze_number(number)
