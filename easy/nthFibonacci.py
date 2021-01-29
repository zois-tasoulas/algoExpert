def nth_fibonacci(number):
    if number < 1:
        raise Exception("Invalid input number given")
    elif number == 1:
        return 0
    else:
        current = 0
        fibonacci_sum = 1
        for _counter in range(3, number + 1):
            previous = current
            current = fibonacci_sum
            fibonacci_sum = previous + current
        return fibonacci_sum


def main():
    print(nth_fibonacci(1))
    print(nth_fibonacci(2))
    print(nth_fibonacci(100))
    print(nth_fibonacci(7))
    print(nth_fibonacci(0))


if __name__ == "__main__":
    main()
