import time

goal = 2020


def main():
    # Prepare an object
    data = import_text()
    data = prepare_data(data)

    for key in data:
        match = goal - int(key)
        if str(match) in data:
            return int(key) * match


def prepare_data(raw_data):
    data = dict()
    for i in raw_data:
        data[i] = i

    return data


def import_text():
    file = open('../../../Inputs/Week1/Day1/puzzle1.txt')
    content = file.read()
    list_ = content.split()
    return list_


def get_answer():
    start = time.time()
    result = main()
    end = time.time()
    runtime = end - start
    return result, runtime


if __name__ == "__main__":
    result, runtime = get_answer()
    print(result)
    print("Took ", runtime, " seconds")

