import json
import os
import sqlite3
import sys
from models import Order, OrderItem


class OrderManager:
    """Manages loading orders from SQLite DB or JSON and computing statistics."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.orders = []
        self.rejected_orders = []
        self.load_data()

    def _read_source(self):
        """Reads raw order records from SQLite database or JSON file."""
        if not os.path.exists(self.filepath):
            print(f"Error: File not found at {self.filepath}")
            sys.exit(1)

        if self.filepath.endswith(".db"):
            try:
                conn = sqlite3.connect(self.filepath)
                cursor = conn.cursor()
                cursor.execute("SELECT id, customer FROM orders ORDER BY id")
                orders_rows = cursor.fetchall()

                data = []
                for order_id, customer in orders_rows:
                    cursor.execute(
                        "SELECT product, price, qty FROM order_items WHERE order_id = ?",
                        (order_id,),
                    )
                    items = []
                    for product, price, qty in cursor.fetchall():
                        parsed_qty = qty
                        if isinstance(qty, str):
                            try:
                                parsed_qty = int(qty)
                            except ValueError:
                                try:
                                    parsed_qty = float(qty)
                                except ValueError:
                                    parsed_qty = qty
                        items.append({
                            "product": product,
                            "price": price,
                            "qty": parsed_qty,
                        })
                    data.append({
                        "id": order_id,
                        "customer": customer,
                        "items": items,
                    })
                conn.close()
                return data
            except sqlite3.Error as e:
                print(f"Error: Invalid or corrupted database at {self.filepath}: {e}")
                sys.exit(1)

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Error: Broken JSON file at {self.filepath}")
            sys.exit(1)

    def load_data(self):
        """Loads orders, separating valid and rejected orders with order ID + reason."""
        data = self._read_source()

        for raw_order in data:
            order_id = raw_order.get("id")
            try:
                customer = raw_order.get("customer")
                raw_items = raw_order.get("items")

                if not isinstance(raw_items, list):
                    raise ValueError("order has no items")

                items = []
                for item in raw_items:
                    items.append(
                        OrderItem(
                            item.get("product"),
                            item.get("price"),
                            item.get("qty"),
                        )
                    )

                order = Order(order_id, customer, items)
                self.orders.append(order)
            except (ValueError, TypeError) as e:
                self.rejected_orders.append({
                    "id": order_id,
                    "raw_data": raw_order,
                    "reason": str(e),
                })

    def total_revenue(self):
        """Returns the sum of all valid orders amounts."""
        return sum(order.total_amount() for order in self.orders)

    def average_order_value(self):
        """Returns the average amount per valid order."""
        if not self.orders:
            return 0.0
        return self.total_revenue() / len(self.orders)

    def top_customer(self):
        """Returns the top customer formatted as 'Name (X orders, Y.YY JOD)'."""
        if not self.orders:
            return "None"
        stats = {}
        for order in self.orders:
            if order.customer not in stats:
                stats[order.customer] = {"count": 0, "total": 0.0}
            stats[order.customer]["count"] += 1
            stats[order.customer]["total"] += order.total_amount()

        top_name = max(stats, key=lambda c: (stats[c]["total"], stats[c]["count"]))
        return f"{top_name} ({stats[top_name]['count']} orders, {stats[top_name]['total']:.2f} JOD)"

    def most_popular_product(self):
        """Returns the best-selling product formatted as 'Product (X units)'."""
        if not self.orders:
            return "None"
        quantities = {}
        for order in self.orders:
            for item in order.items:
                quantities[item.product] = quantities.get(item.product, 0) + item.qty
        if not quantities:
            return "None"
        best_prod = max(quantities, key=quantities.get)
        return f"{best_prod} ({quantities[best_prod]} units)"