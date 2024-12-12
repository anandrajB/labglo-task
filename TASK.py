"""
1. Write a Python function to find the second largest number in a given list (without using reverse operation or sorted function).
2. Write a Python script to read a large text file and return the top 10 most frequent words along with their counts.
3. Write a program to print the following pattern:
   1 2 3 4 5
   1 2 3 4
   1 2 3
   1 2
   1

"""


def second_largest():
    val = [1, 3, 5, 6, 2, 6, 8, 9]
    removed_duplicates = list(set(val))
    return removed_duplicates[::-1][1]


def second_largest2():
    val = [-1, 3, 5, 6, 2, 6, -2, 9, -10]
    removed_duplicates = list(set(val))
    second_value = 0
    for item in removed_duplicates:
        if item > 0 and item is not None:
            second_value = max(second_value, item)
    return second_value


def read_from_file():
    with open("sample.txt", "r") as files:
        values = files.read()
        from collections import Counter

        new_values = Counter(item for item in values.split())
        return [
            {"data": key, "count": value}
            for key, value in new_values.items()
            if value >= 10
        ]


def pattern_print():
    count = 5
    for index, item in enumerate(range(1, int(count) + 1)):
        print(item, end=" ")


print(second_largest())
print(read_from_file())
print(pattern_print())
print(second_largest2())
