# Spark-Declarative-Pipeline-Project

## Executive Summary

This project demonstrates the design and implementation of a modern data platform for a ride-hailing business, inspired by companies like Uber.

Using Databricks Lakeflow Declarative Pipelines (SDP), the project transforms raw trip data into scalable, region-level analytics. The focus is not just on data transformation, but on solving platform challenges such as data latency, pipeline rigidity, and lack of regional insights.

By adopting a declarative approach, the platform enables faster, incremental data processing, reduces manual effort, and delivers timely insights to regional stakeholders.

## Project Overview
This is an end-to-end data engineering project built using:

- Databricks (Free Edition)
- PySpark & Spark SQL
- Lakeflow Declarative Pipelines (SDP)
- Medallion Architecture (Bronze → Silver → Gold)
- Amazon S3 (data source simulation)

The pipeline ingests raw CSV data representing trips and cities, processes it through multiple transformation layers, and produces curated datasets for regional performance analytics.
![ ]()

### 🏢 Business Scenario
A global FMCG enterprise (**Atlikon**) acquired a nutrition startup (**SportsBar**).

- **Atlikon** operates on a modern **Databricks Lakehouse**
- **SportsBar** delivers raw **CSV files in AWS S3**
- No unified or trusted view of **global revenue**

### ❌ The Problem
- Disparate data platforms  
- Dirty, inconsistent schemas  
- No incremental processing  
- No enterprise-level governance  

### ✅ The Solution
Designed and implemented a **scalable, auditable, incremental ELT pipeline** that:
- Ingests startup data from S3
- Cleans and standardizes it
- Merges it into the enterprise **Gold layer**
- Produces a **single source of truth** for analytics


## Key Features / Skills Demonstrated

### Incremental Loading
- Implemented **Staging Table Pattern**
- Processes **only new daily files**
- Recomputes monthly aggregates to handle **late-arriving data**

### Data Quality & Schema Handling
- Schema mismatches handled
- City typos corrected
- Implemented **Dictionary Mapping + Regex Cleaning**

### Orchestration
- Automated Databricks **DAGs**
- Dependency-driven execution:
  - Dimensions → Facts
- Email/Slack alerting on failures

### Auditability & Lineage
- Metadata columns added:
  - `ingestion_timestamp`
  - `file source + name`
- Enables full **data lineage & debugging**

---

## 📂 Repository Structure

```bash
├── 01_setup/
│   ├── 01_setup_catalog.sql              # Unity Catalog schemas & tables
│   ├── 01_dim_date.py                    # Programmatic Date Dimension
│   └── 03_utilities.py                   # Centralized configuration
│
├── 02_dimension_processing/
│   ├── 1_customer_data_processing.py     # Customer cleaning & ID mapping
│   ├── 2_product_data_processing.py      # Regex cleanup & hashing
│   └── 3_pricing_data_processing.py      # Dirty dates & price versioning
│
├── 03_fact_processing/
│   ├── 01_full_load_fact.py              # Historical load
│   └── 02_incremental_load_fact.py       # Daily incremental upsert logic
│
├── 04_denormalized_view/
│   ├── 01_denormalized_table_query.txt   # Combined columns
│   └── 02_parent_incremental_load.txt    # Incremental load of parent data

└── README.md
