import time

request = 'shiny gold bag'

def solve_puzzle():
    # Prepare an object
    data = import_data()
    _result = 0
    for bag in data:
        if contain_bag(data, bag, request):
            _result += 1

    return _result


def contain_bag(data, container, requested):
    # Check whether the bag already contains the requested bag
    bags = data[container]
    for bag_info in bags:
        bag = bag_info['bag']
        if bag == requested:
            return True

        if bag in data:
            if contain_bag(data, bag, requested):
                return True
    return False

def import_data():
    file = open('../../../Inputs/Week2/Day1/input.txt')
    content = file.read()
    list_ = content.split("\n")
    data = dict()
    for i in range(len(list_)):
        written_rule = list_[i]
        container = written_rule.split(' contain ')[0].replace('bags', 'bag')
        contained = written_rule.split(' contain ')[-1][:-1]

        contained = contained.replace('bags', 'bag')
        contained = contained.split(', ')

        for j in range(len(contained)):
            bag = contained[j]
            amount = ''.join(x for x in bag if x.isdigit())
            contained[j] = {
                'bag': bag.replace(amount + " ", ""),
                'amount': amount
            }

        data[container] = contained
    return data


if __name__ == "__main__":
    start = time.time()
    result = solve_puzzle()
    end = time.time()
    print('result', result)
    print("Took ", end-start, " seconds")

