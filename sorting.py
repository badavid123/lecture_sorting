import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_name, mode="r") as file:
        reader = csv.DictReader(file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data


def selection_sort(numbers: list):
    for i in range(len(numbers)):
        smallest_idx = i
        for x in range(i + 1, len(numbers)):
            if numbers[x] < numbers[i]:
                smallest_idx = x
                numbers[i], numbers[smallest_idx] = numbers[smallest_idx], numbers[i]
    return numbers


def bubble_sort(numbers: list):
    n = len(numbers)
    for i in range(n):
        for x in range(0, n-i-1):
            if numbers[x] > numbers[x + 1]:
                numbers[x], numbers[x + 1] = numbers[x + 1], numbers[x]
    return numbers


def insertion_sort(numbers: list):
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i-1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j = j - 1
        numbers[j + 1] = key
    return numbers


def main():
    my_data = read_data("numbers.csv")
    test = my_data["series_1"]
    print(test)
    print(selection_sort(test.copy()))
    print(bubble_sort(test.copy()))
    print(insertion_sort(test.copy()))


if __name__ == '__main__':
    main()
