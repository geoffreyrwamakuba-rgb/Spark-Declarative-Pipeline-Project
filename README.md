# Spark Declarative Pipeline Project

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

![ ](https://github.com/geoffreyrwamakuba-rgb/Spark-Declarative-Pipeline-Project/blob/a00f521355dfc2e9d10525cd4e1c14ce22511619/SDP_data_model.png)
---

### 🏢 Business Scenario

GoodCabs is a fast-growing ride-hailing company operating across multiple cities. Each city functions as an independent region, managed by regional teams responsible for operational performance.

As the business scales, these teams increasingly rely on timely, region-specific data to:
- Monitor revenue and trip volume
- Track customer and driver satisfaction
- Identify underperforming regions
However, the current data platform struggles to meet these needs efficiently.

### ❌ The Problem
The existing system is built on procedural Spark pipelines with manual orchestration, leading to several issues:

- Delayed Data Delivery --> Regional teams are not receiving data on time, limiting decision-making speed
- Lack of Regional Flexibility --> Dashboards are generic, forcing teams to manually extract and reshape data
- Tightly Coupled Pipelines --> Changes are slow and difficult due to rigid pipeline design
- Manual Workarounds --> Teams rely on Excel exports, increasing inefficiency and risk of errors

### ✅ The Solution / Key Benefits of SDP over Imperative Approach
1. Automatic Orchestration
   - No need for manual job scheduling or dependency management
   - Pipelines are automatically executed in the correct order
3. Incremental Processing
   - Only new or updated data is processed
   - Reduces compute cost and improves performance
4. Declarative Simplicity
   - Focus on business logic instead of pipeline control flow
   - Cleaner, more maintainable code
5. Faster Data Delivery --> Reduced latency enables near real-time regional insights
6. Scalability & Flexibility --> Easier to adapt pipelines as business requirements evolve

---

## 📂 Repository Structure

```bash
├── 01_project_setup/         # Unity Catalog schemas & tables
│
├── 02_bronze/
│   ├── city.py 
│   ├── trips.py     
│
├── 03_silver/
│   ├── calendar.py 
│   ├── city.py 
│   ├── trips.py
│   ├── trips2.py     
│
├── 04_gold/ 
│   ├── city_views.sql
│   ├── trips_gold.sql
│
├── 05_data/
│   ├── trips                 # csv files
│   └── city                  # csv files
│
└── README.md
