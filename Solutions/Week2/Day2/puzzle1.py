import time

def solve_puzzle():
    # Prepare an object
    data = import_data()
    accumulator = 0
    indices_passed = []
    index = 0
    while index not in indices_passed:
        instruction_set = data[index]
        instruction = instruction_set['instruction']
        variable = int(instruction_set['variable'])

        if instruction == 'acc':
            accumulator += variable
        elif instruction == 'jmp':
            indices_passed.append(index)
            print(index + 1)
            index += variable
            continue

        indices_passed.append(index)
        index += 1

    return accumulator

def import_data():
    file = open('../../../Inputs/Week2/Day2/input.txt')
    content = file.read()
    list_ = content.split("\n")
    data = []
    for instruction_set in list_:
        instruction = dict()
        instruction['instruction'] = instruction_set[:3]
        instruction['variable'] = instruction_set[4:]
        data.append(instruction)
    return data


if __name__ == "__main__":
    start = time.time()
    result = solve_puzzle()
    end = time.time()
    print('result', result)
    print("Took ", end-start, " seconds")