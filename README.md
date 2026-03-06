# 🚀 Binance Real-Time Data Pipeline & Dual-Model Elastic Net
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## 🏗️ Project Workflow

### 1. C++ Data Collection
* **API Pull:** Pulled Binance API information in C++ using `libcurl`.
* **Processing:** Converted the raw data to **JSON** format.
* **Output:** Pushed the structured data to a **CSV** file.



### 2. Python Orchestration & Database
* **File Management:** Python takes the CSV and **deletes it** immediately after reading.
* **ETL:** Python cleans and processes the CSV data.
* **Storage:** Pushes the finalized data into a **MySQL database**.

---

### 3. Machine Learning & Benchmarking
Once enough data is available in the database, the project moves to the training phase:
* **Dual Training:** I will train the data using my own **hand-coded Elastic Net** and compared against **Scikit-learn’s** version.
* **Live Comparison:** The system will pull new API data and compare the predictions of the two models to see how they perform.



---

## 📂 Project Structure
* `/cppbinace` - C++ Source (libcurl, JSON, CSV Writer)
* `/bianpyt` - Python Scripts (CSV Cleaner, MySQL Connector, ML Models)

---
*Binance Data Engineering & Machine Learning Project*
