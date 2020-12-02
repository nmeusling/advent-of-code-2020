def main():
    expenses = read_expenses_from_file()
    expense_one, expense_two = get_two_numbers_that_sum_2020(expenses)
    print(expense_one, expense_two, expense_two * expense_one)

    expenses = read_expenses_from_file()
    expense_one, expense_two, expense_three =get_three_numbers_that_sum_2020(expenses)
    print(expense_one, expense_two, expense_three, expense_two * expense_one * expense_three)


def read_expenses_from_file():
    with open('expense_report.txt', 'r') as expense_file:
        expenses = expense_file.readlines()
        formatted_expenses = list(map(lambda x: x.rstrip(), expenses))
        formatted_expenses = [int(i) for i in formatted_expenses]
        return formatted_expenses


def get_two_numbers_that_sum_2020(expenses):
    expenses.sort()
    while len(expenses) > 0:
        minimum = expenses[0]
        maximum = expenses[-1]
        sum = minimum + maximum
        # We found the two numbers that sum
        if sum == 2020:
            return minimum, maximum
        # The minimum number is not a possibility, it is too small
        elif sum < 2020:
            expenses.pop(0)
        # The maximum number is not a possibility, it is too big
        else:
            expenses.pop(-1)


def get_three_numbers_that_sum_2020(expenses):
    expenses.sort()
    while len(expenses) > 2:
        # loop through all values, excluding first and last
        mid_number_index = 1
        minimum = expenses[0]
        medium = expenses[mid_number_index]
        maximum = expenses[-1]
        sum = minimum + medium + maximum
        if sum == 2020:
            return minimum, medium, maximum
        # The maximum number is not a possibility, it is too big
        elif sum > 2020:
            expenses.pop(-1)
        # Test the different possible middle numbers
        else:
            while sum < 2020:
                mid_number_index += 1
                medium = expenses[mid_number_index]
                sum = minimum + medium + maximum
                if sum == 2020:
                    return minimum, medium, maximum
            expenses.pop(0)


if __name__ == "__main__":
    main()
