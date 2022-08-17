def is_prime(number):
    if number > 1:
        for num in range(2, int(number**0.5) + 1):
            if number % num == 0:
                return False
        return True
    return False


def main():
    quantity_numbers = int(input("Enter number of numbers to search: "))
    num = 1
    prime_numbers = []
    while quantity_numbers != 0:
        if is_prime(num):
            prime_numbers.append(num)
            quantity_numbers -= 1
        num += 1
    print(prime_numbers)


if __name__ == '__main__':
    main()
