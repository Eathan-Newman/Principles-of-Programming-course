print("What is your first item?", end=" ")
item1_name = input()
print("What is the price of that item?", end=" ")
item1_price = int(input())
print("How many of that item are you purchasing?", end=" ")
item1_quantity = int(input())

item1_subtotal = item1_price * item1_quantity
print(item1_name, "Subtotal:", item1_subtotal)

print("What is your second item?", end=" ")
item2_name = input()
print("What is the price of that item?", end=" ")
item2_price = int(input())
print("How many of that item are you purchasing?", end=" ")
item2_quantity = int(input())

item2_subtotal = item2_price * item2_quantity
print(item2_name, "Subtotal:", item2_subtotal)

cart_total = item1_subtotal + item2_subtotal
print("Cart total:", cart_total)
