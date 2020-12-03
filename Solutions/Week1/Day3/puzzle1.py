import time
import math

right = 3

def solve_puzzle():
    data = get_input()
    result = 0
    for i in range(len(data)):
        place = i * right
        string = data[i]
        if string[place] == "#":
            result += 1

    return result


def get_input():
    file = open('../../../Inputs/Week1/Day3/puzzle1.txt')
    content = file.read()
    list_ = content.split("\n")

    # The required width that will be traversed in a 3, 1 angle
    move_width = len(list_) * right
    for i in range(len(list_)):
        string = list_[i]
        repeats = math.ceil(move_width / len(string))
        list_[i] = list_[i] * repeats
    return list_


if __name__ == "__main__":
    start = time.time()
    result = solve_puzzle()
    end = time.time()
    print(result)
    print("Took ", end-start, " seconds")
