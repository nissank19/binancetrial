# 🚀 Binance Real-Time Data Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/C++%2017-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/python-3.10-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/mysql-%2300758f.svg?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL" />
</p>

A high-performance, containerized hybrid system that tracks **BNB/ETH** trades directly from the Binance API. This project demonstrates a complete data engineering lifecycle: from low-level C++ data ingestion to Python-based ETL and persistent SQL storage.

---

## 🏗 System Architecture

The pipeline is orchestrated with Docker Compose, separating concerns across three core services to maximize performance and maintainability.

<p align="center">
  <img src="https://github.com/nissank19/binancetrial/raw/main/architecture.png" alt="Binance Data Pipeline Architecture" width="700">
</p>

### Service Breakdown:

* **1. 📡 C++ Tracker (`CryptoTracker`)**: Uses high-frequency polling with `libcurl` and `fromId` tracking for resilient data acquisition without duplication.
* **2. 🧹 Python ETL (`Cleaner`)**: A lightweight service using `Pandas` that transforms raw CSV data, cleans time-series data, and applies relational mapping logic.
* **3. 🗄 MySQL Database**: Persistent storage for all historical data, with a volume mapped to `./mysql_data` on your host machine.

---

## 🛠 Tech Stack

| Component | Technology | Primary Role |
| :--- | :--- | :--- |
| **Ingestion** | **C++ 17** | Low-latency API polling |
| **JSON Parser** | `nlohmann/json` | Parse Binance API responses |
| **HTTP Client** | `libcurl` | Network communication |
| **ETL** | **Python 3.10** | Data cleaning & transformation |
| **Processing** | `pandas` | Batch CSV processing |
| **SQL ORM** | `SQLAlchemy` | Database communication |
| **Storage** | **MySQL 8.0** | Persistent trade history |
| **Container** | **Docker** | Isolation and dependency management |

---

## 📊 Data Flow Visualization

The process moves sequentially, with Python acting as the bridge between ephemeral C++ files and the relational database.

<p align="center">
  <img src="https://github.com/nissank19/binancetrial/raw/main/dataflow.png" alt="System Data Flow" width="700">
</p>

---

## 🚦 Getting Started

### Prerequisites
* Docker & Docker Compose
* Git

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/nissank19/binancetrial.git](https://github.com/nissank19/binancetrial.git)
    cd binancetrial
    ```

2.  Spin up the entire pipeline:
    ```bash
    docker-compose up --build -d
    ```

3.  Verify the live data collection (run this to see the row count grow!):
    ```bash
    docker-compose exec db mysql -u root -pwearegoingtomakeit binance -e "SELECT COUNT(*) FROM data;"
    ```

---
*Created by [Your Name] | Data Engineering & Hybrid Systems Performance Study.*
