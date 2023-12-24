import functools


def combine_coins(coin, numbers):
    """
    this func gets a sign and a list of numbers and returns
    a string of each number in the list with the sign appended to it
    :param coin:
    :param numbers:
    :return:
    """
    return ', '.join(coin + str(num) for num in numbers)

def multi_char(char):
    # multiply a char by 2
    return char * 2


def double_letter(my_str):
    # receive a string and returns a string of each char multiplied by 2
    return "".join(map(multi_char, my_str))


def if_div(num):
    # check if a number is not 0 and if number is divided by 4
    return num != 0 and num % 4 == 0


def four_dividers(num):
    # returns a list of all the numbers that are divided by 4 in range 1 - num included
    return list(filter(if_div, range(num+1)))


def add(x, y):
    return int(x) + int(y)


def sum_of_digits(num):
    # sum all the digits of a number
    return functools.reduce(add, str(num))


def main():
    my_list = [x for x in range(6)]
    print(combine_coins('$', my_list))


if __name__ == '__main__':
    main()
