# 🚀 Binance Real-Time Data Pipeline

![C++](https://img.shields.io/badge/C++%2017-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

A high-performance, containerized hybrid system that tracks **BNB/ETH** trades directly from the Binance API. This project demonstrates a complete data engineering lifecycle: from low-level C++ data ingestion to Python-based ETL and persistent SQL storage.

---

## 🏗 System Architecture

The pipeline is orchestrated with Docker Compose, separating concerns across three core services to maximize performance and maintainability.

```text
    ┌────────────────┐      ┌────────────────┐      ┌────────────────┐
    │  Binance API   │ ───> │   C++ Tracker  │ ───> │   Output CSV   │
    └────────────────┘      └────────────────┘      └────────────────┘
                                                            │
                                                            ▼
    ┌────────────────┐      ┌────────────────┐      ┌────────────────┐
    │  MySQL DB (v8) │ <─── │   Python ETL   │ <─── │  File Watcher  │
    └────────────────┘      └────────────────┘      └────────────────┘
