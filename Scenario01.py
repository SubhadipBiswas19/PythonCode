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
        if not name or not category:
            raise ValueError("Name or category cannot be empty")
        if price <= 0:
            raise ValueError("Price cannot be negative or zero")
        if quantity <= 0:
            raise ValueError("Quantity cannot be negative")


        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        Product.total_products += 1

    def update_quantity(self, amount):
        if self.quantity + amount <= 0:
            raise ValueError("Insufficient stock to remove.")
        self.quantity += amount

    def display_details(self):
        print(f"Product Name: {self.name} | Price: ₹{self.price} | Quantity: {self.quantity} | Category: {self.category}")

        @classmethod

        def get_total_products(cls):
            return cls.total_products

    def categorize_products(products):
        for product in products:
            return {category:[p for p in products if p.category == category and p.quantity > 0] for category in set (p.category for p in products)}

    def main(self):

        try:
            p1 = Product("Apple", 10, 100, "Fruit")
            p2 = Product("Milk", 28, 50, "Dairy")
            p3 = Product("Banana", 15, 0, "Fruit")

        except ValueError as e:
            print("Error while creating products:", e)
            return

        products = [p1,p2,p3]

        try:
            p1.update_quantity(10)
            p2.update_quantity(20)
        except ValueError as e:
            print("Error while updating quantity:", e)

            print("\nAll product Details:")
            for p in products:
                p.display_details()

            available_products = [p for p in products if p.quantity > 0]

            categorized = self.categorize_products(available_products)

            print("\nCategorized Products (non-zero quantity):")
            for category, items in categorized.items():
                print(f"\tCategory: {category}")
                for item in items:
                    item.display_details()

            print(f"Total Products: {Product.get_total_products()}")

if __name__ == "__main__":
    p = Product("Apple", 10, 100, "Fruit")
    print(p.display_details())
    print(p.main())