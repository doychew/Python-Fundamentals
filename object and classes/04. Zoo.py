class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}"

        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}"

        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}"


name = input()
rows = int(input())
total_animals = 0
zoo = Zoo(name)

for i in range(rows):
    total_animals += 1
    species, name = input().split()
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))
print(f"Total animals: {total_animals}")