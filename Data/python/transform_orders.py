
import csv
from datetime import datetime

FILE_PATH = r"C:\Users\ajayi\Documents\Brazilian E-commerce Dataset\Data\Raw\olist_orders_dataset.csv"
OUTPUT_PATH = r"C:\Users\ajayi\Documents\Brazilian E-commerce Dataset\Data\Processed\olist_orders_transformed.csv"


def load_orders(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        orders = list(reader)

    return orders


orders = load_orders(FILE_PATH)
def convert_datetime(value):
    if not value:
        return None

    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for order in orders:
    for column in date_columns:
        order[column] = convert_datetime(order[column])


# Calculate delivery days
for order in orders:
    purchase_date = order["order_purchase_timestamp"]
    delivery_date = order["order_delivered_customer_date"]

    if purchase_date is not None and delivery_date is not None:
        order["delivery_days"] = (
            delivery_date - purchase_date
        ).days
    else:
        order["delivery_days"] = None

# Classify delivery performance
for order in orders:
    actual_date = order["order_delivered_customer_date"]
    estimated_date = order["order_estimated_delivery_date"]

    if actual_date is None:
        order["delivery_status"] = "Not Delivered"

    elif actual_date.date() < estimated_date.date():
        order["delivery_status"] = "Early"

    elif actual_date.date() == estimated_date.date():
        order["delivery_status"] = "On Time"

    else:
        order["delivery_status"] = "Late"
print("First order delivery days:", orders[0]["delivery_days"])

print("Orders with delivery days:", sum(
    1 for order in orders if order["delivery_days"] is not None
))

print("Orders without delivery days:", sum(
    1 for order in orders if order["delivery_days"] is None
))

delivery_times = [
    order["delivery_days"]
    for order in orders
    if order["delivery_days"] is not None
]

average_delivery_days = sum(delivery_times) / len(delivery_times)

print("Average delivery time:", round(average_delivery_days, 2), "days")

from collections import Counter

delivery_status_counts = Counter(
    order["delivery_status"] for order in orders
)

print("\nDelivery Status Summary:")

for status, count in delivery_status_counts.items():
    print(f"{status}: {count:,}")
total_orders = len(orders)

print("\nDelivery Performance Percentages:")

for status, count in delivery_status_counts.items():
    percentage = (count / total_orders) * 100
    print(f"{status}: {percentage:.2f}%")

for order in orders:
    actual_date = order["order_delivered_customer_date"]
    estimated_date = order["order_estimated_delivery_date"]

    if actual_date is not None and actual_date.date() == estimated_date.date():
        
        break

fieldnames = list(orders[0].keys())

with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(orders)

print("\nTransformed file saved:", OUTPUT_PATH)