import csv
from oops_Thing import Thing
from oops_Phone import Phone

Thing.instantiate_from_csv()

item = Thing("vase", 300)
item.discount()
item.increament(20)

print(item.price)

phone = Phone('iphone', 400)

phone.discount()


print(phone.price)
