import time
import math

seats_per_column = 8

rowMapping = {
    'F': 0,
    'B': 1,
}

columnMapping = {
    'L': 0,
    'R': 1,
}

def solve_puzzle():
    _result = -1
    data = get_input()
    for i in data:
        # The first 7 characters are the row
        rowCharacters = i[:7][::-1]
        # The last 3 characters are the column
        columnCharacters = i[-3:][::-1]

        row = 0
        for j in range(len(rowCharacters)):
            row += int(math.pow(2, j) * rowMapping[rowCharacters[j]])

        column = 0
        for j in range(len(columnCharacters)):
            column += int(math.pow(2, j) * columnMapping[columnCharacters[j]])

        _id = int(seats_per_column * row + column)
        print(row, column, _id)
        if _id > _result:
            _result = _id
    return _result


def get_input():
    file = open('../../../Inputs/Week1/Day5/input.txt')
    content = file.read()
    list_ = content.split("\n")
    return list_


if __name__ == "__main__":
    start = time.time()
    result = solve_puzzle()
    end = time.time()
    print(result)
    print("Took ", end-start, " seconds")
