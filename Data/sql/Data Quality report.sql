USE Ecom;

GO

SELECT COUNT(*) AS total_orders

FROM dbo.stg_orders_imports;
GO 


-- Check for missing values -- 

SELECT  

    SUM(CASE WHEN order_approved_at IS NULL THEN 1 ELSE 0 END) AS missing_approval,
    SUM(CASE WHEN order_delivered_carrier_date IS NULL THEN 1 ELSE 0 END) AS missing_carrier_date,
    SUM(CASE WHEN order_delivered_customer_date IS NULL THEN 1 ELSE 0 END) AS missing_customer_date

FROM dbo.stg_orders_imports

GO


SELECT 
    order_status, COUNT(*) AS total_orders

FROM dbo.stg_orders_imports

GROUP BY order_status
ORDER BY total_orders DESC;


SELECT
    order_status, COUNT(*) AS total_order_stat,
    SUM(CASE WHEN order_delivered_carrier_date IS NULL THEN 1 ELSE 0 END) AS missing_delivery_date,
    SUM(CASE WHEN order_delivered_customer_date IS NULL THEN 1 ELSE 0 END) AS missing_cust_date

FROM dbo.stg_orders_imports
GROUP BY order_status
ORDER BY total_order_stat DESC;

SELECT
    order_id,
    order_status,
    order_purchase_timestamp,
    order_delivered_carrier_date,
    order_delivered_customer_date
FROM dbo.stg_orders_imports
WHERE order_status = 'delivered'
AND(
    order_delivered_carrier_date IS NULL
    OR order_delivered_customer_date IS NULL
)

SELECT      
    COUNT(*) total_orders,
    COUNT(DISTINCT order_id) AS unique_order_ids

FROM dbo.stg_orders_imports



SELECT
    COUNT(*) AS total_rows,
    SUM(
        CASE
            WHEN order_id IS NULL OR LTRIM(RTRIM(order_id)) = ''
            THEN 1
            ELSE 0
        END
    ) AS missing_or_blank_order_ids
FROM dbo.stg_orders_imports;


SELECT  
    MIN(order_purchase_timestamp) AS first_order_date,
    MAX(order_purchase_timestamp) AS Last_order_date

FROM dbo.stg_orders_imports



USE Ecom;
GO

SELECT
    COUNT(*) AS total_orders,
    SUM(
        CASE
            WHEN order_purchase_timestamp IS NULL
            THEN 1
            ELSE 0
        END
    ) AS missing_purchase_dates
FROM dbo.stg_orders_imports;
