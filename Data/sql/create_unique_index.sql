USE Ecom;
GO

-- Prevents duplicate order IDs in the transformed table.
IF NOT EXISTS (
    SELECT 1
    FROM sys.indexes
    WHERE name = 'UX_orders_transformed_order_id'
      AND object_id = OBJECT_ID('dbo.orders_transformed')
)
BEGIN
    CREATE UNIQUE INDEX UX_orders_transformed_order_id
    ON dbo.orders_transformed (order_id);
END;
GO
