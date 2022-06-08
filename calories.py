from temperature import Temperature

class Calories:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.25 * self.height + 5 - self.temperature * 10
        return result



