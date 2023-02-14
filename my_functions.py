import math


def ratio():
    _PI = math.pi
    _RESTO = math.remainder(33, 2)
    return _PI, _RESTO


""" this function return the content without \n """
def split_lines(content):
    return ''.join(str(content).splitlines())

