# Binance Real-Time Data Pipeline & Predictive Modeling

A multi-stage data engineering project connecting high-performance C++ data collection with Python-based machine learning and MySQL persistence.

## 🏗️ System Architecture & Data Flow

This project implements a complete data lifecycle. The diagram below illustrates how raw API data is ingested by C++, bridged to Python via CSV, cleaned, and persisted in MySQL for analysis.

![[Data Pipeline Flow]](./assets/data_pipeline.png)

---

## 🛠 Project Components

### 1. Data Ingestion (C++)
* **API Integration:** Utilizes `libcurl` to interface with Binance REST/WebSocket endpoints.
* **Data Transformation:** Parses raw responses into **JSON** format.
* **Buffered Output:** Streams processed trade data into local **CSV** files.

### 2. Data Orchestration (Python)
* **File Management:** Python monitors for new CSV files, ingests the data, and **deletes the file** upon successful processing to manage disk overhead.
* **ETL Pipeline:** Handles data normalization, type casting, and feature engineering.
* **Persistence:** Commits cleaned datasets to a **MySQL** database for long-term historical analysis.

---

### 3. Machine Learning & Benchmarking

The final stage is a comparative analysis of regularization techniques, visualizing the tradeoff between L1 (Lasso) and L2 (Ridge) penalties in Elastic Net.

![[Elastic Net Path]](./assets/elastic_net_path.png)

The project implements both:
* **Custom Implementation:** A scratch-built **Elastic Net** regression model.
* **Standard Implementation:** Scikit-learn's `ElasticNet` for benchmarking.

The following chart illustrates the target optimization by comparing the model's predictions (Rule) against the actual Binance trade data (Basis).

![[Prediction vs Actual]](./assets/prediction_vs_actual.png)

---

## 📂 Project Structure
* `/cppbinace` - C++ Source: API clients, JSON parsers, and CSV exporters.
* `/bianpyt` - Python Source: Database connectors, file cleanup logic, and ML model comparisons.
* `/assets` - Directory containing architectural and statistical diagrams.

---

## 🚀 Setup & Execution
1.  **Database:** Ensure MySQL is running and the schema is initialized.
2.  **Producer:** Run the C++ executable to start pulling live data.
3.  **Consumer:** Execute the Python monitoring script to move data from CSV to SQL.
4.  **Analysis:** Run the training scripts once the SQL row count reaches the required threshold.
