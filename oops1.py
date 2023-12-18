class product:
    count = 0
    def __init__(self,name, category,price,):
        self.name = name
        self.category = category
        self.price = price
        product.count = product.count +1
       

    def display_product(self):
        print(f'the {self.category} is {self.name},  price is {self.price} ')

    def sold(self):
        print(self.name, 'has sold')
        product.count = product.count -1


product1 = product('maggie','food', 50)
product2 = product('apple' ,'fruit',100)
product3 = product('milk','drinks', 55)

# product.display_product(product1)
product1.display_product()
product2.display_product()
product3.display_product()

product3.sold()
product1.sold()

print(product.count)
    