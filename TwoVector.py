class TwoVector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return TwoVector(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return TwoVector(self.x - other.x, self.y - other.y)

    def scale(self, number):
        return TwoVector(self.x / number, self.y / number)

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def equals(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


vector_1 = TwoVector(1, 2)
vector_1b = TwoVector(3, 4)
vector_2 = vector_1.add(vector_1b)
vector_sub = vector_1.subtract(vector_1b)
# print(vector_2)
# print(vector_sub)
# print(vector_1b.dot_product(vector_1b))
