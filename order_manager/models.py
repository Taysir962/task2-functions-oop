
from utils import format_price

class OrderItem:
    """Represents an item within an order."""
    def __init__(self, product_name, price, quantity):
        if not product_name or not isinstance(product_name, str):
            raise ValueError("Product name must be a non-empty string.")
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        """Returns the total price for this item (price * quantity)."""
        return self.price * self.quantity


class Order:
    """Represents an order containing multiple items and customer info."""
    def __init__(self, order_id, customer_name, items):
        if not order_id or not isinstance(order_id, str):
            raise ValueError("Order ID must be a non-empty string.")
        if not customer_name or not isinstance(customer_name, str):
            raise ValueError("Customer name must be a non-empty string.")
        if not items or not isinstance(items, list):
            raise ValueError("Order must contain a list of items.")

        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items

    def total_amount(self):
        """Returns the total amount of all items in the order."""
        return sum(item.total_price() for item in self.items)

    def __str__(self):
        return f"Order {self.order_id} by {self.customer_name} - Total: {format_price(self.total_amount())}"