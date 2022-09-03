class Person:
    def __init__(self, name, age, nationality="uk"):
        self.name = name
        self.age = age
        self.nationality = nationality

    def __str__(self):
        return f"A Person {self.name} aged {self.age} from {self.nationality}"

    def __lt__(self, other):
        """Compare two instances of Person by their age.

        Args:
            other (Person) : the other Person instance against to compare

        Returns:
            bool : True if the person's age is smaller than the other person's age. False otherwise.
        """
        return self.age < other.age


assistant1 = Person("Harry", 11, "uk")
assistant2 = Person("Joe", 18, "uk")
print(assistant1 < assistant2)  # should print True
print(assistant2 < assistant1)  # should print False
