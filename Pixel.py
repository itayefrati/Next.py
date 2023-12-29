class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        """
        _x - x coordinate
        _y - y coordinate
        _red - a value between 0 and 255
        _green - a value between 0 and 255
        _blue - a value between 0 and 255
        """
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_cord(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        """
        turns pixel to gray color
        :return:
        """
        sum_gray = self._red + self._blue + self._green
        sum_gray = sum_gray // 3
        self._red = sum_gray
        self._blue = sum_gray
        self._green = sum_gray

    def print_pixel_info(self):
        """
        this function prints all the info of the object Pixel
        :return:
        """
        color = ""
        if self._blue == 0 and self._green == 0 and self._red > 50:
            color = 'Red'
        elif self._red == 0 and self._green == 0 and self._blue > 50:
            color = 'Blue'
        elif self._blue == 0 and self._red == 0 and self._green > 50:
            color = 'Green'
        print('X: ', self._x, ',' ' Y: ', self._y, ',' ' Color: ', (self._red, self._green, self._blue), " ", color, sep="")


def main():
    a = Pixel(5, 6, 250, 0, 0)
    a.print_pixel_info()
    a.set_grayscale()
    a.print_pixel_info()


if __name__ == '__main__':
    main()
