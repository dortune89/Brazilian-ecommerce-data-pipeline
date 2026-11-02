
import csv

FILE_PATH = r"C:\Users\ajayi\Documents\Brazilian E-commerce Dataset\data\raw\olist_orders_dataset.csv"


def load_orders(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        orders = list(reader)
    return orders


def check_missing_values(orders, columns):
    print("\nMissing values by column:")

    for column in columns:
        missing_count = sum(
            1 for order in orders
            if order[column] is None or order[column].strip() == ""
        )
        print(f"{column}: {missing_count}")


def check_order_ids(orders):
    total_orders = len(orders)

    missing_ids = sum(
        1 for order in orders
        if not order["order_id"] or not order["order_id"].strip()
    )

    unique_ids = len({
        order["order_id"].strip()
        for order in orders
        if order["order_id"] and order["order_id"].strip()
    })

    print("\nVALIDATION RESULTS")
    print("-" * 30)
    print("Total orders:", total_orders)
    print("Missing or blank order IDs:", missing_ids)
    print("Unique order IDs:", unique_ids)

    if missing_ids == 0 and unique_ids == total_orders:
        print("PASS: Order IDs are complete and unique.")
    else:
        print("WARNING: Check order IDs for missing values or duplicates.")


orders = load_orders(FILE_PATH)

print("DATA QUALITY REPORT")
print("-" * 30)
print("Total orders:", len(orders))

columns = orders[0].keys()
check_missing_values(orders, columns)
check_order_ids(orders)



