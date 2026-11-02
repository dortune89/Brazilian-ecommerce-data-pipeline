
# Olist E-commerce Data Quality Report

## Dataset Overview

- Dataset: Olist Brazilian E-commerce Public Dataset
- Source file: `olist_orders_dataset.csv`
- Total orders: 99,441
- Date range: September 4, 2016 to October 17, 2018

## Missing Date Investigation

The orders dataset contains missing values in three date columns.

| Column | Missing values |
|---|---:|
| `order_approved_at` | 160 |
| `order_delivered_carrier_date` | 1,783 |
| `order_delivered_customer_date` | 2,965 |

### Missing Approval Dates

The 160 missing approval dates are distributed as follows:

| Order status | Missing approval dates |
|---|---:|
| Canceled | 141 |
| Delivered | 14 |
| Created | 5 |

The 141 canceled orders have no carrier or customer delivery dates. The 5 created orders also have no delivery dates.

The 14 delivered orders have both carrier and customer delivery dates populated. These records are unusual because they reached delivery without a recorded approval timestamp.

### Missing Delivery Dates in Delivered Orders

Among 96,478 delivered orders:

| Delivery-date pattern | Order count |
|---|---:|
| Both dates populated | 96,469 |
| Customer date missing only | 7 |
| Carrier date missing only | 1 |
| Both dates missing | 1 |

Nine delivered orders have at least one missing delivery timestamp. These records should be flagged for further investigation.

### Data Quality Decision

Missing dates will not be replaced with invented timestamps.

Missing values will be preserved in the raw dataset. During the transformation stage, data-quality flags can identify unusual records for further investigation.

## Validation Results

- CSV records: 99,441
- SQL Server records: 99,441
- Unique order IDs: 99,441
- CSV order IDs missing in SQL Server: 0
- Extra SQL Server order IDs: 0

**Result:** CSV and SQL Server order IDs match.
