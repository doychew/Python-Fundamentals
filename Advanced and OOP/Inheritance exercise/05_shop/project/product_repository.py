from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:
    products = []

    def add(self, product: Product):
        ProductRepository.products.append({product.name})

    def find(self, product_name):
        return product_name

    def remove(self, product_name):
        ProductRepository.products.remove(product_name)

    def __repr__(self):
        return f"{''.join(ProductRepository.products)}\n"

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple")
print(repo)
