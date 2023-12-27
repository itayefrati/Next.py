class Octopus:
    def __init__(self, name="Octavio", age=0):
        self._name = name
        self._age = age

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


def main():
    a = Octopus("billy", 18)
    b = Octopus("gilly", 19)
    print(a.get_age())
    print(b.get_age())


if __name__ == '__main__':
    main()
