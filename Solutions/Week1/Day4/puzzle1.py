import time

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def solve_puzzle():
    result = 0
    data = get_input()
    for i in data:
        for j in required:
            if j not in i:
                result += 1
                break

    result = len(data) - result
    return result


def get_input():
    file = open('../../../Inputs/Week1/Day4/puzzle1.txt')
    content = file.read()
    list_ = content.split("\n\n")
    for i in range(len(list_)):
        data = list_[i]
        data = data.replace("\n", " ")
        mydict = dict(e.split(':') for e in data.split(' '))
        list_[i] = mydict
    return list_


if __name__ == "__main__":
    start = time.time()
    result = solve_puzzle()
    end = time.time()
    print(result)
    print("Took ", end-start, " seconds")
