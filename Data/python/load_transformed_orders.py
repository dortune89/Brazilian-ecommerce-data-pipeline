import csv
import pyodbc
import getpass

CSV_FILE = r"C:\Users\ajayi\Documents\Brazilian E-commerce Dataset\Data\Processed\olist_orders_transformed.csv"

def connect_to_database():
    password = getpass.getpass("Enter your SQL Server password: ")

    connection_string = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost,1433;"
        "DATABASE=Ecom;"
        "UID=sa;"
        f"PWD={{{password}}};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    return pyodbc.connect(connection_string, timeout=10)

def read_transformed_orders():
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        orders = list(reader)

    print("CSV file loaded successfully!")
    print("Total records:", len(orders))
    print("Columns:", list(orders[0].keys()))

    return orders
def insert_orders(connection, orders):

    cursor = connection.cursor()

    cursor.execute("SELECT order_id FROM dbo.orders_transformed")
    existing_order_ids = {row[0] for row in cursor.fetchall()}

    insert_query = """
        INSERT INTO dbo.orders_transformed (
            order_id,
            customer_id,
            order_status,
            order_purchase_timestamp,
            order_approved_at,
            order_delivered_carrier_date,
            order_delivered_customer_date,
            order_estimated_delivery_date,
            delivery_days,
            delivery_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    rows = []

    for order in orders:
        if order["order_id"] in existing_order_ids:
            continue

        existing_order_ids.add(order["order_id"])

        rows.append((
            order["order_id"],
            order["customer_id"],
            order["order_status"],
            order["order_purchase_timestamp"] or None,
            order["order_approved_at"] or None,
            order["order_delivered_carrier_date"] or None,
            order["order_delivered_customer_date"] or None,
            order["order_estimated_delivery_date"] or None,
            int(order["delivery_days"]) if order["delivery_days"] else None,
            order["delivery_status"]
        ))

    if rows:
        cursor.fast_executemany = True
        cursor.executemany(insert_query, rows)
        connection.commit()

    print(f"Successfully inserted {len(rows)} records!")

    cursor.close()

if __name__ == "__main__":
    orders = read_transformed_orders()

    connection = connect_to_database()

    print("SQL Server connection successful!")

    insert_orders(connection, orders)

    connection.close()