CREATE TABLE dbo.orders_transformed (
    order_id NVARCHAR(50),
    customer_id NVARCHAR(50),
    order_status NVARCHAR(30),
    order_purchase_timestamp DATETIME2,
    order_approved_at DATETIME2 NULL,
    order_delivered_carrier_date DATETIME2 NULL,
    order_delivered_customer_date DATETIME2 NULL,
    order_estimated_delivery_date DATETIME2,
    delivery_days INT NULL,
    delivery_status NVARCHAR(30)
);

SELECT COUNT(*) AS TotalRecords
FROM dbo.orders_transformed;

SELECT TOP 10
    order_id,
    order_status,
    delivery_days,
    delivery_status
FROM dbo.orders_transformed;

SELECT
    delivery_status,
    COUNT(*) AS TotalOrders
FROM dbo.orders_transformed
GROUP BY delivery_status
ORDER BY TotalOrders DESC;