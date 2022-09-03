import pickle


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector ({self.x}, {self.y})"

    def __repr__(self):
        """This makes the unique string representation
        of the object instance look more readable
        """
        return str(self)


vector1 = Vector(2, 3)
vector2 = Vector(4, 3)
vector = [vector1, vector2]


with open("lesson10/vector.pkl", "wb") as file:
    pickle.dump(vector, file)

with open("lesson10/vector.pkl", "rb") as file:
    pickled_vectors = pickle.load(file)

print(pickled_vectors)
print(type(pickled_vectors))
