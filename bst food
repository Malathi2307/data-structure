class Inventory:
    def __init__(self):
        self.items = {}

    def insert_item(self, item_name, quantity):
        item_name = item_name.lower()
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def delete_item(self, item_name, quantity):
        item_name = item_name.lower()
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                print(f"{quantity} {item_name}(s) deleted.")
                if self.items[item_name] == 0:
                    print(f"{item_name} is now out of stock. Removing from inventory.")
                    del self.items[item_name]
            else:
                print("Not enough quantity in stock.")
        else:
            print("Item not found.")

    def search_item(self, item_name):
        item_name = item_name.lower()
        if item_name in self.items:
            return f"Quantity: {self.items[item_name]}"
        else:
            return "Item not found."

    def traverse(self):
        for item, quantity in self.items.items():
            print(f"Item: {item}, Quantity: {quantity}")

def main():
    inventory = Inventory()
    while True:
        print("\nInventory Management")
        print("1. Insert item")
        print("2. Delete item")
        print("3. Search item")
        print("4. Traverse inventory")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.insert_item(item_name, quantity)
        elif choice == "2":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.delete_item(item_name, quantity)
        elif choice == "3":
            item_name = input("Enter item name: ")
            print(inventory.search_item(item_name))
        elif choice == "4":
            inventory.traverse()
        elif choice == "5":
            print("exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
