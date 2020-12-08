import time

request = 'shiny gold bag'

def solve_puzzle():
    # Prepare an object
    data = import_data()
    return get_content(data, request) - 1


def get_content(data, container):
    total = 0
    bags = data[container]
    for bag_info in bags:
        bag = bag_info['bag']
        amount = bag_info['amount']
        if len(amount) == 0:
            return 1
        else:
            amount = int(amount)
        inner_contained = get_content(data, bag)
        total += amount * inner_contained
    return total + 1


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

