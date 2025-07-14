"""
You are building a simple inventory system for a small store. Each product has a name, price, quantity, and category.
Tasks:
Define a Product class with appropriate instance variables and an __init__ constructor.
Create methods to update quantity (add or remove stock) and display product details.
Maintain a class-level variable to track the total number of products created.
Create a function to accept a list of products and return a dictionary categorizing products by their category using dict comprehension.
Handle exceptions for invalid stock update operations (e.g., negative quantity).
Use list comprehension to filter out products with zero quantity.
Preconditions:
Product name: non-empty string
Price: float > 0
Quantity: int ≥ 0
Category: non-empty string
Quantity update: can add/remove only if resulting quantity ≥ 0
"""
class Product:
    total_products = 0

    def __init__(self, name, price, quantity, category):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if not category:
            raise ValueError("Category cannot be empty.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

        Product.total_products += 1

    def add_stock(self, amount):
        if amount < 0:
            raise ValueError("Cannot add negative stock.")
        self.quantity += amount
        print(f"Added {amount} units to '{self.name}'. Current quantity: {self.quantity}")

    def remove_stock(self, amount):
        if amount < 0:
            raise ValueError("Cannot remove negative stock.")
        if self.quantity - amount < 0:
            raise ValueError("Insufficient stock to remove.")
        self.quantity -= amount
        print(f"Removed {amount} units from '{self.name}'. Current quantity: {self.quantity}")

    def display_details(self):
        print(f"Product: {self.name} | INR {self.price} | Qty: {self.quantity} | Category: {self.category}")

    @classmethod
    def get_total_products(cls):
        return cls.total_products


def categorize_by_category(products):
    return {category: [p for p in products if p.category == category] for category in set(p.category for p in products)}


def filter_out_of_stock(products):
    return [p for p in products if p.quantity > 0]

def filter_in_stock(products):
    return [p for p in products if p.quantity <= 0]


if __name__ == "__main__":

    p1 = Product("Milk", 40.0, 100, "Dairy")
    p2 = Product("Curd", 30.0, 0, "Dairy")
    p3 = Product("Apple", 80.0, 25, "Fruits")
    p4 = Product("Orange", 60.0, 0, "Fruits")

    p1.remove_stock(10)
    p3.add_stock(15)

    for p in [p1, p2, p3, p4]:
        p.display_details()

    print("\nIn-stock:")
    for p in filter_out_of_stock([p1, p2, p3, p4]):
        p.display_details()

    print("\nOut of stock:")
    for p in filter_in_stock([p1, p2, p3, p4]):
        p.display_details()

    print("\nCategorized Products:")
    categorized = categorize_by_category([p1, p2, p3, p4])
    for category, items in categorized.items():
        print(f"Category: {category}")
        for item in items:
            print(f"  - {item.name}")

    print(f"\nTotal products created: {Product.get_total_products()}")
