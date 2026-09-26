# Data Analyzer and Transformer Program

def input_data():
    data = input("\nEnter data for a 1D array (separated by spaces): ")

    try:
        numbers = list(map(int, data.split()))

        if len(numbers) == 0:
            print("Error: Please enter at least one number.")
            return None

        print("\nData has been stored successfully!")
        return numbers

    except ValueError:
        print("\nError: Please enter numbers only.")
        return None


def display_summary(data):
    print("\nData Summary:")
    print("- Total elements:", len(data))
    print("- Minimum value:", min(data))
    print("- Maximum value:", max(data))
    print("- Sum of all values:", sum(data))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def filter_data(data):
    try:
        threshold = int(input("\nEnter threshold value: "))

        # Lambda function
        filtered_data = list(filter(lambda x: x > threshold, data))

        print("\nFiltered Data:")
        print(filtered_data)

    except ValueError:
        print("Error: Please enter a valid number.")


def sort_data(data):
    print("\nOriginal Data:")
    print(data)

    ascending = sorted(data)
    descending = sorted(data, reverse=True)

    print("\nAscending Order:")
    print(ascending)

    print("\nDescending Order:")
    print(descending)


def dataset_statistics(data):
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)

    return minimum, maximum, total, average


def main():
    data = []

    print("")
    print(" Welcome to the Data Analyzer and Transformer")
    print("")

    while True:

        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-In Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = input("\nPlease enter your choice: ")

        # Option 1
        if choice == "1":
            new_data = input_data()

            if new_data is not None:
                data = new_data

        # Option 2
        elif choice == "2":
            if len(data) == 0:
                print("\nPlease enter data first.")
            else:
                display_summary(data)

        # Option 3
        elif choice == "3":
            try:
                number = int(input("\nEnter a number to calculate factorial: "))

                if number < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    result = factorial(number)
                    print(f"\nFactorial of {number} = {result}")

            except ValueError:
                print("Error: Please enter a valid number.")

        # Option 4
        elif choice == "4":
            if len(data) == 0:
                print("\nPlease enter data first.")
            else:
                filter_data(data)

        # Option 5
        elif choice == "5":
            if len(data) == 0:
                print("\nPlease enter data first.")
            else:
                sort_data(data)

        # Option 6
        elif choice == "6":
            if len(data) == 0:
                print("\nPlease enter data first.")
            else:
                minimum, maximum, total, average = dataset_statistics(data)

                print("\nDataset Statistics:")
                print("- Minimum value:", minimum)
                print("- Maximum value:", maximum)
                print("- Sum of all values:", total)
                print("- Average value:", round(average, 2))

        # Option 7
        elif choice == "7":
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter a number from 1 to 7.")

# Start program
main()