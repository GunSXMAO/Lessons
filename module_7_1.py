import os
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        if not os.path.exists(self.__file_name):
            return ""

        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()

        return products

    def add(self, *products):
        if os.path.exists(self.__file_name):
            file = open(self.__file_name, 'r')
            current_products = set(file.read().splitlines())
            file.close()
        else:
            current_products = set()

        file = open(self.__file_name, 'a')
        for product in products:
            product_str = str(product)
            if product_str not in current_products:
                file.write(product_str + '\n')
                current_products.add(product_str)
            else:
                print(f'Продукт {product_str} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
