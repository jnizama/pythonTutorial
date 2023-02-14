# examples how use collections in python

def join_lists():
    customers1 = ["John", "Peter", "Paul"]  # lists
    customers2 = ["Marie", "Victoria", "Laura", ["mario", "jimenez"]]  # lists
    customers = customers1 + customers2
    return customers


def simple_tuple():
    taxes = ("IGV", "ICP", "IVA", "RTN")
    return taxes

def simple_dictionary():
    countries = {"PE": "Peru", "UK": "United Kingdom", "GE":"Germany", "RU": "Russian"}
    return countries

def compose_dictionary():
    person = {"name": "John", "address": {"city": "Mi Peru", "country": "Peru"}}
    return person
