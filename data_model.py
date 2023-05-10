from datetime import datetime

class Product:
    def __init__(self, title, description, price, available_date, stock_quantity, product_type):
        self.title = title
        self.description = description
        self.price = price
        self.available_date = available_date
        self.stock_quantity = stock_quantity
        self.product_type = product_type

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display(self):
        return self.products

    def search_products(self, keyword):
        return [product for product in self.products if keyword.lower() in product.title.lower()]

    def filter_products(self, criteria):
        if criteria == 'newest':
            return sorted(self.products, key=lambda product: product.available_date, reverse=True)
        elif criteria == 'oldest':
            return sorted(self.products, key=lambda product: product.available_date)
        elif criteria == 'in_stock':
            return [product for product in self.products if product.stock_quantity > 0]
        elif criteria == 'out_of_stock':
            return [product for product in self.products if product.stock_quantity == 0]

class MicroStore(Store):
    def __init__(self, name):
        super().__init__(name)

    def add_promotional_product(self, product):
        self.add_product(product)

    # Method overriding from base class Store to display only promotional products
    def display(self):
        return [product for product in self.products if product.product_type == 'promotional']


class Storefront(Store):
    def __init__(self, name):
        super().__init__(name)


if __name__ == '__main__':
    
    # Example usage:
    # Create some products
    product1 = Product("Shirt", "Comfortable cotton shirt", 19.99, datetime(2023, 1, 1), 10, 'promotional')
    product2 = Product("Mug", "High-quality ceramic mug", 9.79, datetime(2023, 3, 15), 0, 'customized')
    product3 = Product("Cap", "Stylish baseball cap", 14.00, datetime(2023, 2, 10), 5, 'normal')

    # Create a MicroStore and add promotional products
    microstore = MicroStore("MicroStore 1")
    microstore.add_promotional_product(product1)
    microstore.add_promotional_product(product2)
    microstore.add_promotional_product(product3)

    results = microstore.display()
    print("\n\nDisplay (MicroStore):")
    for product in results:
        print(product.title, end = ', ')

    # Create a Storefront and add products
    storefront = Storefront("Storefront 1")
    storefront.add_product(product1)
    storefront.add_product(product2)
    storefront.add_product(product3)

    # Display inventory items in  Storefront
    results = storefront.display()
    print("\n\nDisplay (Storefront):")
    for product in results:
        print(product.title, end = ', ')


    # Search and filter products
    search_results = storefront.search_products("shirt")
    print("\n\nSearch results: ", )
    for product in search_results:
        print(product.title)

    filter_results = storefront.filter_products("in_stock")
    print("\nFilter results: items in_stock")
    for product in filter_results:
        print(product.title)

    filter_results = storefront.filter_products("newest")
    print("\nFilter results: newest on top to oldest")
    for product in filter_results:
        print(product.title)

    filter_results = storefront.filter_products("oldest")
    print("\nFilter results: oldest on top to newest")
    for product in filter_results:
        print(product.title)



