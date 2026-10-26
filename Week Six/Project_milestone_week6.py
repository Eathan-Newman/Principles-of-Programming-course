class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        item_found = False

        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break

        if item_found == False:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        item_found = False

        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                item.item_quantity = modified_item.item_quantity
                item_found = True
                break

        if item_found == False:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_items = 0

        for item in self.cart_items:
            total_items = total_items + item.item_quantity

        return total_items

    def get_cost_of_cart(self):
        total_cost = 0.0

        for item in self.cart_items:
            item_cost = item.item_price * item.item_quantity
            total_cost = total_cost + item_cost

        return total_cost

    def print_total(self):
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")

        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    choice = ""

    while choice != "q":
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output item descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        print("\nChoose an option:", end=" ")
        choice = input()

        if choice == "a":
            print("\nADD ITEM TO CART")

            new_item = ItemToPurchase()

            print("Enter the item name:", end=" ")
            new_item.item_name = input()

            print("Enter the item description:", end=" ")
            new_item.item_description = input()

            print("Enter the item price:", end=" ")
            new_item.item_price = float(input())

            print("Enter the item quantity:", end=" ")
            new_item.item_quantity = int(input())

            cart.add_item(new_item)

        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")

            print("Enter name of item to remove:", end=" ")
            item_name = input()

            cart.remove_item(item_name)

        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")

            modified_item = ItemToPurchase()

            print("Enter the item name:", end=" ")
            modified_item.item_name = input()

            print("Enter the new quantity:", end=" ")
            modified_item.item_quantity = int(input())

            cart.modify_item(modified_item)

        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == "q":
            print("Thank you for shopping!")

        else:
            print("Invalid option. Please try again.")


print("Enter customer's name:", end=" ")
customer_name = input()

print("Enter today's date:", end=" ")
current_date = input()

shopping_cart = ShoppingCart(customer_name, current_date)

print(f"\nCustomer name: {customer_name}")
print(f"Today's date: {current_date}")

print_menu(shopping_cart)
