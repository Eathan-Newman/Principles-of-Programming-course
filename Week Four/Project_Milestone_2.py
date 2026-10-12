class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

cart_items = []
cart_total = 0.0

while True:
    print("Enter an item name (or 'quit' to finish):", end=" ")
    item_name = input()

    if item_name == "quit":
        break

    new_item = ItemToPurchase()
    new_item.item_name = item_name

    print("Enter the item price:", end=" ")
    new_item.item_price = float(input())
    print("Enter the item quantity:", end=" ")
    new_item.item_quantity = int(input())

    cart_items.append(new_item)

print("--TOTAL COST--")

for item in cart_items:
    item.print_item_cost()
    cart_total = cart_total + item.item_price * item.item_quantity

print(f"Cart Total: ${cart_total:.2f}")