#!/usr/bin/python3
""" Square Module """


class Square():
    """ Square class """
    __width = 0
    __height = 0

    def __init__(self, *args, **kwargs):
        """ Constructor """
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if type(value) is int:
            self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if type(value) is int:
            self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.__width * self.__width

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ String representation """
        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
