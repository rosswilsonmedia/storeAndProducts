from classes.store import Store
from classes.products import Products

walmart=Store('Walmart')
paperTowels=Products('Paper Towels', 1.50, 'Essentials')
toiletPaper=Products('Toilet Paper', 1.25, 'Essentials')
iceCream=Products('Ice Cream', 3.25, 'Frozen Food')

walmart.add_product(paperTowels).add_product(toiletPaper).add_product(iceCream).sell_product(1).inflation(.35).set_clearance('Essentials', .25)
for product in walmart.products:
    product.print_info()