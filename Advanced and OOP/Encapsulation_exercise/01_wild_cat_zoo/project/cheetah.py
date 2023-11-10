from project.animal import Animal


# if it dont run change money for care only at int
class Cheetah(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, money_for_care=60)
