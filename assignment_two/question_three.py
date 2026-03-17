def get_number():
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Invalid input. Please enter a positive integer.")
            return None
        return n
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None


def generate_pyramid(n):
    for i in range(1, n + 1):

        # Increasing numbers
        for j in range(1, i + 1):
            print(j, end="")

        # Decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")

        print()  # move to next line


def main():
    n = get_number()
    if n is not None:
        generate_pyramid(n)


main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
