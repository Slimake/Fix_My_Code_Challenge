#!/usr/bin/python3
"""
Square Module
"""


class Square():
    """
    Attr:
        width
        height
    Methods:
        __init__(self, *args, **knwargs)
        area(self)
        perimeter(self)
        __str__(self)
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initialize square instance with width and height """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        if self.width != self.height:
            self.height = self.width
            return self.width * self.height
        else
            return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=30, height=40)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
