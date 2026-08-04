# Brayan Penaherrera, 04/27/26, BrayanPenaherrera_PE7_2.py
# This program asks for a number greater than 25 and displays the prime and composite numbers up to that number, with no more 
# than 10 numbers per line.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_numbers(limit):
    primes = []
    composites = []

    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
        else:
            composites.append(num)

    return primes, composites


def print_list(numbers):
    count = 0
    for num in numbers:
        print(num, end=" ")
        count += 1
        if count == 10:
            print()
            count = 0
    if count != 0:
        print()


def main():
    while True:
        user_input = input("Enter an integer greater than 25: ")

        if user_input == "":
            break

        num = int(user_input)

        if num <= 25:
            print("Please enter a number greater than 25.")
            continue

        primes, composites = get_numbers(num)

        print(f"\nFor numbers ranging from 2 to {num}")
        print("These are prime numbers: ")
        print_list(primes)

        print("These are composite numbers: ")
        print_list(composites)

        again = input(
            "\ntest more numbers 1=yes or press Enter to end program: ")
        if again != "1":
            break


main()
