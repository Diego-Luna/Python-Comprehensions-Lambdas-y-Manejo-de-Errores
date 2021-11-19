def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'Diego', 'lastname': 'Luna'}

    super_list = [
        {'firstname': 'Diego', 'lastname': 'Luna'},
        {'firstname': 'Francisco', 'lastname': 'Lopez'},
        {'firstname': 'Annabeth', 'lastname': 'Chase'},
        {'firstname': 'Anna', 'lastname': 'Luna Lopez'},
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-2, -1, 0, 1, 2],
        'floating_nums': [-2.2, -1.1, 0, 1.2, 2.1]
    }

    for key, value in super_dict.items():
        print(key, '-', value)


if __name__ == '__main__':
    run()
