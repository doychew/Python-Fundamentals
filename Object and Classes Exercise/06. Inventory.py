class Inventory:

    def __init__(self, __capacity):
        self.__capacity = int(__capacity)
        self.items = []

    def get_capacity(self):
        return self.__capacity

    def add_item(self, item):
        if len(self.items) == self.__capacity:
            return "not enough room in the inventory"
        self.items.append(item)

    def __repr__(self):
        left_capacity = self.__capacity - len(self.items)
        return f"Items: {', '.join(self.items)}.\nCapacity left: {left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
