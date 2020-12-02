import time

def solve_puzzle():
    data = get_input()
    result = 0
    for i in data:
        ranges = i[0].split("-")
        bottom_range = int(ranges[0])
        top_range = int(ranges[1])
        letter = i[1][0]
        password = i[2]

        count = password.count(letter)
        if bottom_range <= count <= top_range:
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
