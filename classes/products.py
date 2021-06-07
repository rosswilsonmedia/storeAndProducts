class Products:
    __product_id=1
    def __init__(self, name, price, category):
        self.name=name
        self.price=price
        self.category=category
        self.id=Products.__product_id
        Products.increment_product_id()
    def update_price(self, percent_change, is_increased):
        if is_increased==False:
            self.price=round(self.price*(1-percent_change),2)
        else:
            self.price=round(self.price*(1+percent_change),2)
        return self
    def print_info(self):
        print(f"{self.name}\n${self.price}\n{self.category}\n{self.id}")
        return self
    @classmethod
    def increment_product_id(cls):
        cls.__product_id+=1

