'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''

class Beer:
    """
        Types of beers

    """
    beverage = ["Alcohlic", "Non-Alcohlic"]
    container = ["Glass", "Bottle", "Can"]

    def __init__(self, name ="unavailable", category="IPA", percentage=5, company="Budwieser"):
        self.name = name
        self.category = category
        self.percentage = percentage
        self.company = company

    def __str__(self):
        return f"{self.name} |{self.category} | {self.percentage} | {self.compnay}"


    def print_beer(self):
        print(f"{self.name} is a(n) {self.category} with a {self.percentage} alcohol content and is made by {self.company}")

class Turds:

    """
    The mean green matter that no one talks about

    """
    brand = ["own", "others"]
    location = ["toliet", "outside toliet"]

    def __init__(self, color = "brown", smell = "putrid", consistency = "solid" )
        self.color = color
        self.smell = smell
        self.consistency = consistency

    def __str__(self):
        return f"{self.color} | {self.smell} | {self.consistency}"

    def print_Turds(self):
        print(f"This turd is {self.color} and smells {self.smell} with a consistency of {self.consistency})"






