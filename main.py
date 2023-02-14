
from my_collections import *
from functionsmix import *
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

    #loops
    # for i in simple_tuple():
    #    print(i)

    # for a in range(0,5):
    #    print(a)

    # for w in {"code": 1, "code2":5, "code3":"red"}:
    #    print(w)

    # getting more one value from a function (AWESOME...)
    x_PI, y_RESTO = ratio()
    print(x_PI)
    print(y_RESTO)