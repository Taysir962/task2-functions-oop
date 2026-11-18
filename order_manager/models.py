from utils import format_price


class OrderItem:
    """Represents an item within an order."""

    def __init__(self, product, price, qty):
        if not product or not isinstance(product, str) or not product.strip():
            raise ValueError("product name is empty")

        if (
            not isinstance(price, (int, float))
            or isinstance(price, bool)
            or price <= 0
        ):
            raise ValueError(f"price must be positive ({product})")

        if not isinstance(qty, int) or isinstance(qty, bool) or qty <= 0:
            raise ValueError(f"quantity must be a positive whole number ({product})")

        self.product = product.strip()
        self.price = float(price)
        self.qty = qty

    def total_price(self):
        """Returns the total price for this item (price * qty)."""
        return self.price * self.qty


class Order:
    """Represents an order containing multiple items and customer info."""

    def __init__(self, order_id, customer, items):
        if not isinstance(order_id, int) or isinstance(order_id, bool) or order_id <= 0:
            raise ValueError("order id must be a positive integer")

        if not isinstance(customer, str) or not customer.strip():
            raise ValueError("customer name is empty")

        if not items or not isinstance(items, list):
            raise ValueError("order has no items")

        self.id = order_id
        self.customer = customer.strip()
        self.items = items

    def total_amount(self):
        """Returns the total amount of all items in the order."""
        return sum(item.total_price() for item in self.items)

    def __str__(self):
        return f"Order {self.id} by {self.customer} - Total: {format_price(self.total_amount())}"