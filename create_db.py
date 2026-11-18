import json
import sqlite3


conn = sqlite3.connect("data/orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product TEXT,
    price REAL,
    qty TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(id)
)
""")

cursor.execute("DELETE FROM order_items")
cursor.execute("DELETE FROM orders")

with open("data/orders.json", "r", encoding="utf-8") as f:
    orders_data = json.load(f)

for order in orders_data:
    cursor.execute(
        "INSERT INTO orders (id, customer) VALUES (?, ?)",
        (order["id"], order["customer"])
    )
    for item in order["items"]:
        cursor.execute(
            "INSERT INTO order_items (order_id, product, price, qty) VALUES (?, ?, ?, ?)",
            (order["id"], item["product"], item["price"], str(item["qty"]))
        )

conn.commit()

cursor.execute("SELECT COUNT(*) FROM orders")
count = cursor.fetchone()[0]

conn.close()
print(f"Done! Inserted {count} orders into data/orders.db")