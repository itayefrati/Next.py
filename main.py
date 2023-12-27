import functools
# import string


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


def intersection(list_1, list_2):
    # returns a list of the common items between two lists
    return list(set(list_1).intersection(set(list_2)))


def is_prime(number):
    # check if a number is a prime number
    return (number > 1) and not (True in [number % y == 0 for y in range(2, number)])


def is_funny(my_string):
    # check if a string is only combined from a and h
    return (len(my_string) > 1) and not (True in [char != 'a' and char != 'h' for char in my_string])


def longest_name(file):
    # this function returns the longest word in a text file
    with open(file, "r") as file_object:
        return max(word for word in file_object)


def sum_len(file):
    # this function sums the length of words in a text file
    with open(file, "r") as f:
        return sum(len(word) for word in f.read().split())


def shortest_name(file):
    # this function returns the shortest word in a file
    with open(file, "r") as f:
        lst = sorted(f.read().split(), key=len)
        result = (word for word in lst if len(word) == len(lst[0]))
        return '\n'.join(result)


def create_new_file(file):
    with open(file, "r") as f:
        with open("name_length.txt", "w") as f2:
            return f2.write('\n'.join(str(len(name)) for name in f.read().split()))


def main():
    """password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    print("".join((chr(ord(char) + 2)) if char in string.ascii_lowercase else char for char in password))"""

    file = r"C:\Users\User\Documents\names.txt"
    with open(file, "r") as f:
        names = f.read()
        # 1: this code returns the longest word in a text file
        "print(max(word for word in names.split()))"

        # 2: this code sums the length of words in a text file
        "print(sum(len(word) for word in names.split()))"

        # 3: this code returns the shortest word in a file
        """lst = sorted(names.split(), key=len)
        result = (word for word in lst if len(word) == len(lst[0]))
        print('\n'.join(result))"""

        # 4: this code copies the lengths of words in file to another text file
        """with open("name_length.txt", "w") as f2:
            f2.write('\n'.join(str(len(name)) for name in names.split()))"""

        # 5: this code prints all the words from a text file with the given len
        """num = input("enter a number: ")
        chosen_names = '\n'.join(name for name in names.split() if len(name) == int(num))
        print(str(chosen_names))"""


if __name__ == '__main__':
    main()
