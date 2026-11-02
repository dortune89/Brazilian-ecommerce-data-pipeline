
import getpass
import pyodbc


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


def check_orders(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) AS total_orders,
            COUNT(DISTINCT order_id) AS unique_order_ids
        FROM dbo.stg_orders_imports;
    """)

    result = cursor.fetchone()

    print("Database query successful!")
    print("Total orders:", result[0])
    print("Unique order IDs:", result[1])

    cursor.close()


try:
    with connect_to_database() as connection:
        check_orders(connection)

except pyodbc.Error as error:
    print("Database operation failed:")
    print(error)
