import random

doors = [0, 1, 2]
gifts = ['goat', 'goat', 'car']


def game_initialize():
    random.shuffle(doors)
    random.shuffle(gifts)
    dic = dict(zip(doors, gifts))
    # print(dic)
    return dic


# game_initialize()

def game_body(dictionary):
    print('===================================')
    '''
        选手选择第一扇门
    '''
    first_key = input('Choose a door to open:')
    first_value = dictionary[int(first_key)]
    # print(first_value)

    '''
        主持人打开有goat的一扇门
    '''
    del [dictionary[int(first_key)]]
    # print(dictionary)
    goat_key = list(dictionary.keys())[list(dictionary.values()).index('goat')]
    print('"goat" behind the door ' + str(goat_key))

    '''
        选手选择是否更换为第三扇门
    '''
    del [dictionary[int(goat_key)]]
    # print(dictionary)
    second_key = dictionary.keys()
    # print(list(second_key)[0])
    choice = input('Switch to ' + str(list(second_key)[0]) + '?(y/n)')
    if (choice == 'y'):
        second_value = dictionary[list(second_key)[0]]
        if (second_value == 'car'):
            print('You Win!')
        else:
            print('You Lose!')
    if (choice == 'n'):
        if (first_value == 'car'):
            print('You Win!')
        else:
            print('You Lose!')

    return


game_body(game_initialize())
while (input('Do you want to try once more?(y/n)') == 'y'):
    game_body(game_initialize())

