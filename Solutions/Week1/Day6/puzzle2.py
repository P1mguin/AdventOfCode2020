import time

def solve_puzzle():
    data = get_input()
    groups = []
    for group in data:
        answer = None
        for person in group:
            person_set = set(person)
            if answer is None:
                answer = person_set
            else:
                answer = set(person_set.intersection(answer))

        groups.append(len(answer))

    _result = 0
    for group in groups:
        _result += group
    return _result


def get_input():
    file = open('../../../Inputs/Week1/Day6/input.txt')
    content = file.read()
    list_ = content.split("\n\n")
    data = []
    for i in range(len(list_)):
        data.append(list_[i].split("\n"))
    return data


if __name__ == "__main__":
    start = time.time()
    result = solve_puzzle()
    end = time.time()
    print('result', result)
    print("Took ", end-start, " seconds")
