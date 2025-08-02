# the key parameter can be used to sort complex objects


class Product():
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def __repr__(self):
        return repr((self.name, self.price))

    def discount_price(self):
        return self.price - (self.price * self.discount)


prodlist = [
    Product("Widget", 50, 0.05),
    Product("Doohickey", 40, 0.15),
    Product("Thingamabob", 35, 0.0),
    Product("Gadget", 65, 0.20)
]

# TODO: use the key parameter to select a field to sort on


# TODO: define a lambda function as the sorting key


# TODO: the key parameter can also call a method on the object

