import math
from typing import Dict, List


Mayan_Numeral = str

BASE: int = 20


def read_num(numeral_dict: Dict[Mayan_Numeral, int], height: int) -> List[int]:
    numeral: Mayan_Numeral = ""
    num_list: List[int] = []

    nb_lines: int = int(input())
    for i in range(nb_lines):
        num_line: str = input()
        numeral += num_line
        numeral += '\n'
        if i % height == height - 1:
            # last column
            number: int = numeral_dict[numeral]
            num_list.append(number)
            numeral = ""  # reset
    return num_list[::-1]


def convert_base20_to_10(num_list: List[int]) -> int:
    number: int = 0
    i: int = len(num_list) - 1
    while i >= 0:
        number += num_list[i] * math.pow(BASE, i)
        i -= 1
    return number


def convert_base10_to_20(number: int) -> List[int]:
    num_list: List[int] = []
    # avoid division by 0
    if number == 0:
        num_list.append(0)
        return num_list

    while number != 0:
        num_list.append(number % BASE)  # remainder
        number //= BASE

    return num_list[::-1]


if __name__ == "__main__":
    width, height = map(int, input().split())
    numerals: List[Mayan_Numeral] = []
    numeral_dict: Dict[Mayan_Numeral, int] = {}  # mayan numeral => base 20 number

    for _ in range(height):
        row: Mayan_Numeral = input()
        numerals.append(row)

    # Store the mayan numerals in a dictionary
    for i in range(BASE):
        numeral: Mayan_Numeral = ""
        column: int = i * width
        for row in numerals:
            for j in range(column, column + width):
                numeral += row[j]
            numeral += '\n'
        numeral_dict[numeral] = i

    # Read the 2 numbers
    num_list1: List[int] = read_num(numeral_dict, height)
    num_list2: List[int] = read_num(numeral_dict, height)

    num1: int = convert_base20_to_10(num_list1)
    num2: int = convert_base20_to_10(num_list2)

    operation: str = input()

    # Calculate the result of the operation in base 10
    result: int = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    else:
        result = num1 / num2

    # Convert the result back to the original base
    num_list: List[int] = convert_base10_to_20(result)
    for number in num_list:
        for (numeral, n) in numeral_dict.items():
            if n == number:
                print(numeral, end='')
