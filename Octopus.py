class Octopus:
    # count the number of objects created from this class
    count_animals = 0

    def __init__(self, name="Octavio", age=0):
        """
        :param name: name of the object
        :param age: age of the object in numbers
        """
        self._name = name
        self._age = age
        Octopus.count_animals += 1

    def birthday(self):
        # age + 1
        self._age += 1

    def get_age(self):
        # return current age
        return self._age

    def set_name(self, name):
        # set a different name
        self._name = name

    def get_name(self):
        # return current name
        return self._name


def main():
    a = Octopus("billy")
    print(a.get_name())
    b = Octopus()
    print(b.get_name())
    b.set_name('dildo')
    print(b.get_name())
    print(Octopus.count_animals)


if __name__ == '__main__':
    main()
