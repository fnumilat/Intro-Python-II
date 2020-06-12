# Base Class/ Parent Class
class Product:
    def __init__(self, name, price, discount = 0):
        self.name = name
        self.price = price
        self.discount = discount

    def __str__(self):
        return f'{self.name}: ${self.price} (great deal)'
    
# Child Class that Inherits from PRODUCT
class Sneaker(Product):
    def __init__(self, price, name, shoe_size, brand):
        # super() returns us the parent class instance
        super().__init__(name, price, 0)
        self.shoe_size = shoe_size
        self.brand = brand

class SoccerBall(Product):
    def __init__(self, name, price, material):
        super().__init__(name, price, 10)
        self.material = material

    # Override the Product str function with our own     
    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} WILSOOOOONNNNNNNNNN'
    
    def kick(self):
        print("The ball flew away")
    

generic_product = Product("Generic Thing", "99.99")
print(generic_product)

nike_free = Sneaker("100", "Nike Free", "10", "Nike")
soccer_ball = SoccerBall("Wilson", "20", "Rubber")

# Nike free will use the Product __Str__ function
print(nike_free)
# Soccer ball wiull use the SoccerBall __Str__function
print(soccer_ball)
soccer_ball.kick()