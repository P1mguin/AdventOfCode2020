import time

def solve_puzzle():
    data = get_input()
    result = 0
    for i in data:
        ranges = i[0].split("-")
        first = int(ranges[0]) - 1
        last = int(ranges[1]) - 1
        letter = i[1][0]
        password = i[2]

        first_letter = password[first] == letter
        last_letter = password[last] == letter
        if (first_letter or last_letter) and not (first_letter and last_letter):
            result += 1
    return result


def get_input():
    file = open('../../../Inputs/Week1/Day2/puzzle1.txt')
    content = file.read()
    list_ = content.split("\n")
    for i in range(len(list_)):
        elem = list_[i].split(" ")
        list_[i] = elem
    return list_


if __name__ == "__main__":
    start = time.time()
    result = solve_puzzle()
    end = time.time()
    print(result)
    print("Took ", end-start, " seconds")
