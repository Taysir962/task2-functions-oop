import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from manager import OrderManager
from utils import format_price


def main():
    if len(sys.argv) < 2:
        print("Usage: python order_manager/main.py <path_to_db_or_json>")
        sys.exit(1)

    data_path = sys.argv[1]
    manager = OrderManager(data_path)

    total_orders = len(manager.orders) + len(manager.rejected_orders)
    valid_orders = len(manager.orders)
    rejected_orders = len(manager.rejected_orders)

    print(f"=== Order Report: {data_path} ===")
    print(f"Orders: {total_orders} total | {valid_orders} valid | {rejected_orders} rejected")
    print(f"Revenue: {format_price(manager.total_revenue())} | Average order: {format_price(manager.average_order_value())}")
    print(f"Top customer: {manager.top_customer()}")
    print(f"Best-selling product: {manager.most_popular_product()}")
    print("Rejected orders:")
    for rej in manager.rejected_orders:
        print(f"  #{rej['id']}: {rej['reason']}")


if __name__ == "__main__":
    main()