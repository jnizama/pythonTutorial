""" Writing text in files """


def write_file(path):
    f = open(path, "w")  # open a file for writing
    f.write("I like this Margot")


def read_file(path):
    f = open(path)
    return f.read()


def read_on_file(path):
    f = open(path)
    return f.readline()
