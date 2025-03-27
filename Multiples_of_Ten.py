def is_list_mult10(my_list):
    for num in my_list:
        if num % 10 != 0:
            return False
    return True

def is_list_no_mult10(my_list):
    for num in my_list:
        if num % 10 == 0:
            return False
    return True

if __name__ == '__main__':
    list_size = int(input())
    my_list = [int(input()) for i in range(list_size)]

    if is_list_mult10(my_list):
        print('all multiples of 10')
    elif is_list_no_mult10(my_list):
        print('no multiples of 10')
    else:
        print('mixed values')