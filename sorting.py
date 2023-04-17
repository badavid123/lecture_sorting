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


def main():
    my_data = read_data("numbers.csv")
    test = my_data["series_1"]
    print(test)
    print(selection_sort(test.copy()))


if __name__ == '__main__':
    main()
