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

# use the key parameter to select a field to sort on
def prodsort(product):
    return product.price


print(sorted(prodlist, key=prodsort))

# use the key parameter to select a field to sort on
print(sorted(prodlist, key=lambda p: p.name))

# the key parameter can also call a method on the object
print(sorted(prodlist, key=lambda p: p.discount_price()))
