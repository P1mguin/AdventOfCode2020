import time
import copy

mapping = {
    'nop': 'jmp',
    'jmp': 'nop',
}

def solve_puzzle():
    # Prepare an object
    data = import_data()
    accumulator = 0
    indices_passed = []
    index = 0
    while index < len(data):
        instruction_set = data[index]
        instruction = instruction_set['instruction']
        variable = int(instruction_set['variable'])

        if instruction == 'jmp' or instruction == 'nop':
            without_change = run_program(index, data, copy.deepcopy(indices_passed), accumulator)

            instruction = mapping[instruction]
            data[index] = {
                'instruction': instruction,
                'variable': variable,
            }

            with_change = run_program(index, data, copy.deepcopy(indices_passed), accumulator)

            if with_change[1] and not without_change[1]:
                return with_change[0]
            else:
                instruction = mapping[instruction]

        if instruction == 'acc':
            accumulator += variable
        elif instruction == 'jmp':
            indices_passed.append(index)
            index += variable
            continue

        indices_passed.append(index)
        index += 1


def run_program(index, data, indices_passed, accumulator):
    while index < len(data) and index not in indices_passed:
        instruction_set = data[index]
        instruction = instruction_set['instruction']
        variable = int(instruction_set['variable'])

        if instruction == 'acc':
            accumulator += variable
        elif instruction == 'jmp':
            indices_passed.append(index)
            index += variable
            continue

        indices_passed.append(index)
        index += 1

    return accumulator, index == len(data)

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