import time

def solve_puzzle():
    data = get_input()
    groups = []
    for group in data:
        all_questions = ""
        for person in group:
            all_questions += person
        groups.append(len("".join(set(all_questions))))

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
    print(result)
    print("Took ", end-start, " seconds")
