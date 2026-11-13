
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from manager import OrderManager
from utils import format_price

if __name__ == "__main__":
    print("=== Order Manager Report ===")
    
    data_path = os.path.join(os.path.dirname(__file__), "orders.json")
    manager = OrderManager(data_path)
    
    print(f"Total Valid Orders: {len(manager.orders)}")
    print(f"Total Revenue: {format_price(manager.total_revenue())}")
    print(f"Average Order Value: {format_price(manager.average_order_value())}")
    print(f"Top Customer: {manager.top_customer()}")
    print(f"Most Popular Product: {manager.most_popular_product()}")
    
    print("-" * 30)
    print(f"Rejected / Invalid Orders: {len(manager.rejected_orders)}")
    for rej in manager.rejected_orders:
        print(f"Reason: {rej['reason']}")