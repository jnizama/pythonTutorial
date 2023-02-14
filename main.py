import sys
import os

from my_collections import *
from my_functions import *
from my_classes import *
from files import *
from environment import *

FILE = "d:\\hosts"


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def function_customer() -> list[str]:
    customers1 = ["John", "Peter", "Paul"]  # lists
    customers2 = ["Marie", "Victoria", "Laura", ["mario", "jimenez"]]  # lists
    customers = customers1 + customers2
    return customers


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # simple_dictionary = simple_dictionary()
    # myPeru = simple_dictionary["PE"]
    person = compose_dictionary()
    name = person['name']
    # print(name)

    # getting nested element
    country = person['address']['country']
    # print(country)

    ifcountry = person.get("names", "nada")
    # print(ifcountry)

    # loops
    # for i in simple_tuple():
    #    print(i)

    # for a in range(0,5):
    #    print(a)

    # for w in {"code": 1, "code2":5, "code3":"red"}:
    #    print(w)

    # getting more one value from a function (AWESOME...)
    x_PI, y_RESTO = ratio()
    # print(x_PI)
    # print(y_RESTO)

    person1 = Person("John", "Connor", 60)
    isOld = person1.is_mayor_age()
    print(isOld)

    show_mass_body = person1.mass_body(175, 85)
    print(show_mass_body)

    # write_file("d:\hosts")
    # Read all content of a file from a path
    # data = read_file(FILE)

    # Read one line of a file from a path
    data = read_on_file(FILE)
    data = data.replace("\n","") # removing character new line (\n)
    # print(data)

    # removing all new line (\n) from a file
    data_without_newlines = read_file(FILE)
    final = []
    for s in data_without_newlines:
        final.append(s.replace("\n",""))
    # print(final)

    # using only strip remove leading and trailing whitespace
    data_without_newline = read_file(FILE)
    final = data_without_newline.strip()
    #print(final2)

    # using split lines
    data = read_file(FILE)
    final = split_lines(data)
    # print(final)
    x = 74
    # print('this is my %d' % 17.05)

    # write operative system
    # print(get_operative_system_v1())
    # print(get_operative_system_v2())

    # list files of my documents
    path = os.environ['USERPROFILE']
    files = get_all_files_from__my_documents()
    for file in files:
        print(file)