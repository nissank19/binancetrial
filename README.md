# 🚀 Binance Real-Time Data & Dual-Model Elastic Net
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## 🏗️ The Data Pipeline
This project implements a full-cycle automated trading data pipeline, bridging high-performance systems with statistical analysis.

### 1. Data Ingestion (C++)
* **Fetcher:** Uses `libcurl` to pull real-time market information from the Binance API.
* **Serialization:** Converts raw API responses into structured **JSON**.
* **Storage:** Pushes the processed data into a local **CSV** file for the Python consumer.

### 2. Processing & Storage (Python)
* **File Handling:** Python monitors the directory, ingests the CSV, and **immediately deletes it** to maintain a clean state.
* **Data Cleaning:** Cleans and prepares the features (Price, Quantity, Time) for the database.
* **Database:** Pushes the final cleaned dataset into a **MySQL** database for long-term persistence.

### 3. Machine Learning (The Dual-Fit Strategy)
Once sufficient data is accumulated in MySQL, the system performs a comparison study:
* **Custom Model:** A hand-coded **Elastic Net** implementation.
* **Scikit-Learn:** The industry-standard `sklearn.linear_model.ElasticNet`.
* **Verification:** The system pulls new live API data and compares the predictive accuracy of both models.

---

## 🧠 Discrete Math Applications (The "Big 7")
This architecture serves as a practical lab for the following Discrete Mathematics concepts:

* **Q4: Relations** – Mapping API JSON objects to SQL relational table rows.
* **Q5: Induction** – The recursive cycle of CSV generation ($P(n)$) and deletion ($P(n+1)$).
* **Q6: Modulo** – Transforming Unix timestamps into cyclical time features using $t \pmod{24}$.
* **Q7: Resolution** – Using **L1 Regularization** to "resolve" and eliminate non-significant market features.

---

## 📂 Project Structure
* `/cppbinace` - C++ Source (libcurl, JSON, CSV Writer)
* `/bianpyt` - Python Scripts (CSV Cleaner, MySQL Connector, ML Models)

---
*Developed as part of the "Big 7" Discrete Math Study Project.*
