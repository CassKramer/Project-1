# Name:
# OSU Email:
# Course:       CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    """
    Find the min and max values from a given array and return values as a tuple
    """
    array_1 = arr.length()

    min = arr.get(0)
    max = arr.get(0)

    for index in range(1, array_1):
        if arr.get(index) < min:
            min = arr.get(index)

        if arr.get(index) > max:
            max = arr.get(index)

    return min, max



# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Modifies a static array of integers depending on the divisibility of the numbers and returns a new object
    """

    array_1 = arr.length()
    new_array = StaticArray(array_1)

    for index in range(0, array_1):
        if arr.get(index) % 3 == 0 and arr.get(index) % 5 != 0:
            new_array.set(index, 'fizz')

        elif arr.get(index) % 5 == 0 and arr.get(index) % 3 != 0:
            new_array.set(index, 'buzz')

        elif arr.get(index) % 5 == 0 and arr.get(index) % 3 == 0:
            new_array.set(index, 'fizzbuzz')

        else:
            new_array.set(index, arr.get(index))


    return new_array



# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Reverses the order of elements in a static array
    """
    array_1 = arr.length()
    for index in range(array_1 // 2):
        values = arr[index]
        arr[index] = arr[array_1 - index - 1]
        arr[array_1 - index - 1] = values





# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Receives static array and steps as parameters, and moves the values in static array the value of steps
    """
    array_1 = arr.length()

    new_array = StaticArray(array_1)
    for index in range(0, array_1):
        if steps >= 0:
            if index + steps < array_1:
                new_array.set(index + steps, arr.get(index))
                if index < array_1 - 1:
                    index += 1

            else:
                new_index = steps % array_1
                if new_index + index < array_1:
                    new_array.set(index + new_index, arr.get(index))
                    if index < array_1 - 1:
                        index += 1
                else:
                    next_index = (new_index + index) - array_1
                    new_array.set(next_index, arr.get(index))
                    if index < array_1 - 1:
                        index += 1
        else:
            if index + steps >= 0:
                new_array.set(index + steps, arr.get(index))
                if index < array_1 - 1:
                    index += 1
            else:
                new_index = abs(steps) % array_1
                if index - new_index >= 0:
                    new_array.set(index - new_index, arr.get(index))
                    if index < array_1 - 1:
                        index += 1
                else:
                    next_index = (index - new_index) + array_1
                    new_array.set(next_index, arr.get(index))
                    if index < array_1 - 1:
                        index += 1

    return new_array




# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Uses two integers; start and end and returns the consecutive integers between those values
    """

    range = abs((end - start)) + 1
    new_array = StaticArray(range)
    new_array.set(0, start)
    value = 1
    index = 1

    if start == end:

        return new_array

    while start + value != end and start - value != end:
        if end - start < 0:
            new_array.set(index, start - value)
            value += 1
            index += 1
        else:
            new_array.set(index, start + value)
            value += 1
            index += 1

    if start + value == end and start != value:
        new_array.set(index, end)
    elif start - value == end and start != value:
        new_array.set(index, end)

    return new_array


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Receives a static array and returns an integer based on whether the array is sorted and how it is sorted
    """
    array_1 = arr.length()

    for index in range(0, array_1):
        if array_1 == 1:
            return 1
        while index < array_1 - 1:
            if arr[index] < arr[index + 1]:
                index += 1
                if index == array_1 - 1:
                    return 1
                if arr[index] > arr[index + 1]:
                    return 0

            elif arr[index] > arr[index + 1]:
                index += 1
                if index == array_1 - 1:
                    return -1
                if arr[index] < arr[index + 1]:
                    return 0

            else:
                return 0


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    finds the mode in a given array and returns it and the number of times it appears
    """
    counter = 1
    mode = arr[0]
    array_1 = arr.length()
    for index in range(0, array_1):
        if index == array_1 - 1:
            return mode, counter
        if arr[index] == arr[index + 1]:
            mode = arr[index]
            index += 1
            counter += 1
        if (array_1 - 1) - index <= counter and index == array_1 - 1:
            return mode, counter
        if (array_1 - 1) - index <= counter and arr[index] != arr[index + 1]:
            return mode, counter

    return mode, counter



    pass

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Removes any numbers that are duplicates in a given array and returns a new array without duplicates
    """
    count = arr.length()
    length_array = arr.length()

    for index in range(0, length_array):
        if length_array == 1:
            new_array = StaticArray(count)
            new_array.set(0, arr.get(0))
            return new_array

        if index != length_array - 1:
            if arr[index] == arr[index + 1]:
                count -= 1

    new_array = StaticArray(count)
    new_array.set(0, arr.get(0))
    value = 1

    for index in range(0, length_array):
        if index == length_array - 1:
            new_array.set(value, arr.get(index))
            return new_array
        if index == length_array - 1:
            if arr[index] != arr[index - 1]:
                new_array.set(value, arr.get(index))
                return new_array
        if arr[index] != arr[index + 1]:
            if index != 0 or 1:
                new_array.set(value, arr.get(index))
                value += 1

    return new_array



# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
