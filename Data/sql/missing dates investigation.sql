SELECT 
order_status, COUNT(*) AS missing_approval_date
FROM dbo.stg_orders_imports
WHERE order_approved_at IS NULL 
GROUP BY order_status
ORDER BY missing_approval_date DESC;

SELECT
    order_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
FROM dbo.stg_orders_imports
WHERE order_status = 'delivered'
AND order_approved_at IS NULL 
ORDER BY order_purchase_timestamp;


SELECT
    order_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date

FROM dbo.stg_orders_imports

WHERE order_status = 'created' AND 
order_approved_at IS NULL;


SELECT
    order_id,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
FROM dbo.stg_orders_imports

WHERE order_status = 'canceled' AND 
order_approved_at IS NULL; 


SELECT
    order_status,
    COUNT(*) AS missing_carrier_dates
FROM dbo.stg_orders_imports
WHERE order_delivered_carrier_date IS NULL 
GROUP BY order_status
ORDER BY missing_carrier_dates DESC;


SELECT
    order_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
FROM dbo.stg_orders_imports
WHERE order_status = 'delivered' AND 
order_delivered_carrier_date IS NULL;


SELECT
    order_status,
    COUNT(*) AS missing_customer_delivery_date
from dbo.stg_orders_imports
WHERE order_delivered_customer_date IS NULL 
GROUP BY order_status
ORDER BY missing_customer_delivery_date DESC;


SELECT
    order_id,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
FROM dbo.stg_orders_imports
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NULL;



    

     SELECT
        CASE
            WHEN order_delivered_carrier_date IS NULL AND order_delivered_customer_date IS NULL THEN 'Both dates missing'
            WHEN order_delivered_carrier_date IS NULL AND order_delivered_customer_date IS NOT NULL THEN 'Carrrier date missing only'
            WHEN order_delivered_carrier_date IS NOT NULL AND order_delivered_customer_date IS NULL THEN 'Customer date missing only'
        ELSE 'Both dates populated' END AS Delivery_date_pattern,
        COUNT(*) AS order_count

    FROM dbo.stg_orders_imports
    WHERE order_status = 'delivered'
    GROUP BY 
        CASE
            WHEN order_delivered_carrier_date IS NULL AND order_delivered_customer_date IS NULL THEN 'Both dates missing'
            WHEN order_delivered_carrier_date IS NULL AND order_delivered_customer_date IS NOT NULL THEN 'Carrrier date missing only'
            WHEN order_delivered_carrier_date IS NOT NULL AND order_delivered_customer_date IS NULL THEN 'Customer date missing only'
        ELSE 'Both dates populated' END
    ORDER BY order_count DESC;