
import json
from models import Order, OrderItem

class OrderManager:
    """Manages loading orders from JSON and computing statistics and analytics."""
    def __init__(self, filepath):
        self.filepath = filepath
        self.orders = []
        self.rejected_orders = []
        self.load_data()

    def load_data(self):
        """Loads orders from JSON file, separating valid and invalid/rejected orders."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            for raw_order in data:
                try:
                    order_id = raw_order.get("order_id")
                    customer_name = raw_order.get("customer_name")
                    raw_items = raw_order.get("items", [])
                    
                    items = []
                    for item in raw_items:
                        items.append(OrderItem(
                            item.get("product_name"),
                            item.get("price", 0),
                            item.get("quantity", 0)
                        ))
                    
                    order = Order(order_id, customer_name, items)
                    self.orders.append(order)
                except (ValueError, TypeError) as e:
                    self.rejected_orders.append({
                        "raw_data": raw_order,
                        "reason": str(e)
                    })
        except FileNotFoundError:
            print(f"Error: File not found at {self.filepath}")

    def total_revenue(self):
        """Returns the sum of all valid orders amounts."""
        return sum(order.total_amount() for order in self.orders)

    def average_order_value(self):
        """Returns the average amount per valid order."""
        if not self.orders:
            return 0.0
        return self.total_revenue() / len(self.orders)

    def top_customer(self):
        """Returns the customer name with the highest total spending."""
        if not self.orders:
            return None
        spending = {}
        for order in self.orders:
            spending[order.customer_name] = spending.get(order.customer_name, 0) + order.total_amount()
        return max(spending, key=spending.get)

    def most_popular_product(self):
        """Returns the product name with the highest total quantity sold."""
        if not self.orders:
            return None
        quantities = {}
        for order in self.orders:
            for item in order.items:
                quantities[item.product_name] = quantities.get(item.product_name, 0) + item.quantity
        if not quantities:
            return None
        return max(quantities, key=quantities.get)