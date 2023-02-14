class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name= first_name
        self.last_name = last_name
        self.age = age

    def to_string(self):
        return "The name is: " + self.first_name + " with lastname " + self.last_name + " and year " + self.date_birth

    def is_mayor_age(self) -> bool:
        if self.age >= 60:
            return True
        else:
            return False

    ## Using exceptions
    def mass_body(self, height, weight) -> int:
        try:
            mass = (height / weight)
            return mass
        except ZeroDivisionError:
            """ Exist many kind of errors to exceptions """
            """ for example TypeError, ValueError """
            raise ValueError("Expected value weight")
