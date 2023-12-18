class product:
    count = 0
    def __init__(self,name,category,price,):
        self.name = name
        self.category = category
        self.price = price
        product.count = product.count +1

    def display_product(self):
        print(f'{self.name} is a {self.category} , and the price is {self.price}')

    def sold(self):
        print(self.name, 'has sold')
        product.count = product.count -1


product1 = product('SUPRAA', 'CAR',9999999)
product2 = product('APPLE','FRUIT',100)
product3 = product('KTM','BIKE',199999)

product1.display_product()
product2.display_product()
product3.display_product()

product2.sold()
product1.sold()


print(product.count)