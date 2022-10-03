from cgi import print_arguments


def hello():
    print("Hello instructor, I am a python file. However, I am a computer so I am not actually sure what I am.")


hello()


def pack(item_one, item_two, item_three):
    return [item_one, item_two, item_three]


def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print('You have successfully completed the strenous task of eating.')
    else:
        for i in range(len(lunch_items)):
            if i == 0:
                print(f'First I eat {lunch_items[0]}')
            else:
                print(f'Next I eat {lunch_items[i]}')


print(pack('item_one', 'item_two', 'item_three'))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(['Spearmint Gum', 'Craig Boar Ribs', 'Murloc Eyes'])
