# Brazilian E-Commerce Data Engineering Pipeline

## 1. Project Overview

This project demonstrates an end-to-end data engineering workflow using the Brazilian E-Commerce Public Dataset by Olist.

The objective is to extract, inspect, clean, transform, validate, and load e-commerce order data using Python and Microsoft SQL Server, then store the transformed dataset in Amazon S3.

The project also demonstrates data quality assessment, basic business analysis, database integration, and cloud storage automation.

## 2. Technologies Used

- Python
- Microsoft SQL Server
- SQL
- pyodbc
- Boto3
- Amazon S3
- AWS CLI
- Docker
- Visual Studio Code
- Microsoft Excel

## 3. Dataset Description

**Source:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

The project uses the Olist e-commerce orders dataset.

The original orders dataset contains:

- 99,441 records
- 8 original columns
- Order information, customer references, order status, and timestamps

The dataset contains missing delivery and approval dates, which were investigated during the data quality assessment.

## 4. Project Workflow

### Stage 1: Data Extraction and Inspection

- Loaded the original CSV dataset.
- Inspected column names and data types.
- Checked missing values and duplicate records.
- Investigated missing order dates.
- Confirmed 99,441 unique order IDs.

### Stage 2: Data Transformation Using Python

Created Python scripts to:

- Load the original CSV dataset.
- Convert timestamp columns into datetime values.
- Handle missing date values.
- Calculate delivery duration in days.
- Classify orders as Early, Late, On Time, or Not Delivered.
- Export the transformed dataset to CSV.

### Stage 3: SQL Server Integration

- Created the Ecom database.
- Created staging and transformed tables.
- Loaded the transformed CSV into SQL Server using Python and pyodbc.
- Implemented duplicate protection in the Python loader.
- Created a unique index on order_id to prevent duplicate records.
- Validated record counts and delivery classifications.

### Stage 4: Data Validation

- Confirmed 99,441 records in the source and transformed datasets.
- Verified that all order IDs were present and unique.
- Compared Python and SQL Server delivery classifications.
- Confirmed that grouped delivery status counts matched.
- Verified that the SQL table contained exactly 99,441 unique records.

### Stage 5: Cloud Storage Using Amazon S3

- Created a private Amazon S3 bucket.
- Configured an IAM user with restricted S3 upload permissions.
- Installed and configured AWS CLI.
- Used Python Boto3 to automate uploading the transformed CSV file to Amazon S3.
- Verified successful upload to the S3 bucket.
- Kept public access blocked to protect the dataset.

## 5. Key Business Findings

The Python transformation produced the following delivery classifications:

| Delivery Status | Number of Orders | Percentage |
|---|---:|---:|
| Early | 88,649 | 89.15% |
| Late | 6,535 | 6.57% |
| On Time | 1,292 | 1.30% |
| Not Delivered | 2,965 | 2.98% |
| **Total** | **99,441** | **100%** |

Additional findings:

- Average delivery duration: 12.09 days.
- Orders with recorded customer delivery dates: 96,476.
- Orders without recorded customer delivery dates: 2,965.

The average delivery duration is calculated using the 96,476 orders with recorded customer delivery dates.

Percentages are calculated against all 99,441 orders.

## 6. Project Structure

```text
Brazilian E-commerce Dataset/
│
├── .vscode/
│   └── settings.json
│
├── Data/
│   ├── Raw/
│   │   └── Original Olist CSV datasets
│   │
│   ├── Processed/
│   │   └── olist_orders_transformed.csv
│   │
│   ├── python/
│   │   ├── inspect_orders.py
│   │   ├── transform_orders.py
│   │   ├── validate_pipeline.py
│   │   ├── test_sql_connection.py
│   │   ├── load_transformed_orders.py
│   │   └── upload_to_s3.py
│   │
│   └── sql/
│       ├── Data Quality report.sql
│       ├── missing dates investigation.sql
│       ├── orders_transformed.sql
│       └── USE Ecom;.sql
│
├── data_quality_report.md
└── README.md
```

## 7. Project Status

- [x] Dataset inspection and quality assessment
- [x] Python data transformation
- [x] Transformed CSV export
- [x] SQL Server integration
- [x] Data validation
- [x] Duplicate protection
- [x] Amazon S3 bucket creation
- [x] Automated Python upload to S3 using Boto3
- [ ] Publish project to GitHub

## 8. Dataset Attribution and License

**Dataset:** Brazilian E-Commerce Public Dataset by Olist.

**Source:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

**License:** CC BY-NC-SA 4.0.

This project uses the dataset for educational and portfolio purposes. Refer to the original dataset license for attribution, non-commercial use, and redistribution requirements.
