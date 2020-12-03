import time
import math


def solve_puzzle(right, down):
    data = get_input(right, down)
    result_ = 0
    for i in range(0, len(data), down):
        place = int((i * right)/down)
        string = data[i]
        if string[place] == "#":
            result_ += 1

    return result_


def get_input(right, down):
    file = open('../../../Inputs/Week1/Day3/puzzle1.txt')
    content = file.read()
    list_ = content.split("\n")

    # The required width that will be traversed in a 3, 1 angle
    move_width = (len(list_) * right) / down
    for i in range(len(list_)):
        string = list_[i]
        repeats = math.ceil(move_width / len(string))
        list_[i] = list_[i] * repeats
    return list_


if __name__ == "__main__":
    start = time.time()
    one = solve_puzzle(1, 1)
    three = solve_puzzle(3, 1)
    five = solve_puzzle(5, 1)
    seven = solve_puzzle(7, 1)
    two = solve_puzzle(1, 2)
    result = one * three * five * seven * two
    end = time.time()
    print(result)
    print("Took ", end-start, " seconds")
