
import csv

FILE_PATH = r"C:\Users\ajayi\Documents\Brazilian E-commerce Dataset\data\raw\olist_orders_dataset.csv"


def load_orders(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames
        orders = list(reader)

    return orders, columns


def check_data_quality(orders, columns):
    print("DATA QUALITY REPORT")
    print("-" * 30)
    print("Total CSV orders:", len(orders))

    print("\nMissing values by column:")

    for column in columns:
        missing_count = sum(
            1 for order in orders
            if not order[column] or not order[column].strip()
        )
        print(f"{column}: {missing_count}")
    print("\nMISSING DATE SUMMARY")
    print("-" * 30)

    date_columns = [
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date"
    ]

    for column in date_columns:
        missing_count = sum(
            1 for order in orders
            if not order[column] or not order[column].strip()
        )

        print(f"{column}: {missing_count} missing")
        
    order_ids = [
        order["order_id"].strip()
        for order in orders
        if order["order_id"] and order["order_id"].strip()
    ]

    missing_ids = len(orders) - len(order_ids)
    unique_ids = len(set(order_ids))

    print("\nORDER ID VALIDATION")
    print("-" * 30)
    print("Missing or blank IDs:", missing_ids)
    print("Unique order IDs:", unique_ids)

    if missing_ids == 0 and unique_ids == len(orders):
        print("PASS: Order IDs are complete and unique.")
    else:
        print("WARNING: Check for missing or duplicate order IDs.")



import getpass
import pyodbc

def get_sql_order_ids(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT order_id
        FROM dbo.stg_orders_imports;
    """)

    order_ids = {
        row[0].strip()
        for row in cursor.fetchall()
        if row[0]
    }

    cursor.close()
    return order_ids

def check_sql_server(csv_count):
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

    with pyodbc.connect(connection_string, timeout=10) as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM dbo.stg_orders_imports;
        """)

        sql_count = cursor.fetchone()[0]
        sql_order_ids = get_sql_order_ids(connection)
        print("Unique SQL order IDs:", len(sql_order_ids))
        
        csv_order_ids = {
            order["order_id"].strip()
            for order in load_orders(FILE_PATH)[0]
            if order["order_id"] and order["order_id"].strip()
        }

        missing_in_sql = csv_order_ids - sql_order_ids
        extra_in_sql = sql_order_ids - csv_order_ids

        print("CSV order IDs missing in SQL:", len(missing_in_sql))
        print("Extra SQL order IDs:", len(extra_in_sql))

        if not missing_in_sql and not extra_in_sql:
            print("PASS: CSV and SQL order IDs match.")
        else:
            print("WARNING: CSV and SQL order IDs do not match.")

        cursor.close()
        

        print("\nDATABASE VALIDATION")
        print("-" * 30)
        print("CSV orders:", csv_count)
        print("SQL Server orders:", sql_count)

        if csv_count == sql_count:
            print("PASS: CSV and SQL Server record counts match.")
        else:
            print("WARNING: CSV and SQL Server counts do not match.")

orders, columns = load_orders(FILE_PATH)
check_data_quality(orders, columns)
check_sql_server(len(orders))


def get_sql_order_ids(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT order_id
        FROM dbo.stg_orders_imports;
    """)

    order_ids = {row[0].strip() for row in cursor.fetchall() if row[0]}
    cursor.close()

    return order_ids

