import time
from matplotlib.colors import is_color_like

required = [{
    'value': 'byr',
    'ranges': {
        'default': {
            'min': 1920,
            'max': 2002,
        },
    },
}, {
    'value': 'iyr',
    'ranges': {
        'default': {
            'min': 2010,
            'max': 2020,
        }
    }
}, {
    'value': 'eyr',
    'ranges': {
        'default': {
            'min': 2020,
            'max': 2030,
        }
    }
}, {
    'value': 'hgt',
    'ranges': {
        'cm': {
            'min': 150,
            'max': 193,
        },
        'in': {
            'min': 59,
            'max': 76,
        }
    }
}, {
    'value': 'hcl',
    'hard-coded': True
}, {
    'value': 'ecl',
    'options': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
}, {
    'value': 'pid',
    'hard-coded': True
}]


def solve_puzzle():
    result = 0
    data = get_input()
    for i in data:
        print(i)
        for j in required:
            # Check whether the value is actually contained
            key = j['value']
            if key not in i:
                result += 1
                print('not in i', key, i)
                break

            value = i[key]

            # Check for the minimum and maximum value
            if 'ranges' in j:
                unit = value[-2] + value[-1]
                ranges = j['ranges']
                if unit not in ranges:
                    unit = 'default'
                else:
                    value = value[:-2]

                if 'default' not in ranges and unit not in ranges:
                    result += 1
                    print('no unit', value, unit)
                    break

                min = ranges[unit]['min']
                max = ranges[unit]['max']
                value = int(value)
                if value < min or value > max:
                    result += 1
                    print('value too high / low', min, value, max, unit)
                    break


            # Check whether you gave up on regex -> True
            if 'hard-coded' in j:
                if key == 'hcl':
                    if value[0] != '#' or not is_color_like(value):
                        result += 1
                        print("No colour", value)
                        break

                if key == 'pid':
                    if len(value) != 9:
                        result += 1
                        print("No length 9", value)
                        break

                    try:
                        int(value)
                    except ValueError:
                        result += 1
                        print("No integer", value)
                        break

            # Check whether there are defined options in the regex
            if 'options' in j:
                if not value in j['options']:
                    print("Value not an option'", value, j['options'])
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
    print("Took ", end - start, " seconds")
