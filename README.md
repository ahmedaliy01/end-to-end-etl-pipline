<div align="center">

# ⚡ Dockerized MySQL ETL Pipeline

### *An End-to-End Data Engineering Pipeline for Automated Extraction, Cleaning, and Relational Database Loading*

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Overview

**Dockerized MySQL ETL Pipeline** is a robust Data Engineering solution designed to automate the extraction, transformation, and ingestion of raw unstructured datasets into a relational database system.

The project demonstrates a production-like containerized workflow: reading non-standard encoded CSV files, enforcing strict schema standardization, handling URL-safe credentials, and streaming transformed batches into a **Dockerized MySQL 8.0** instance using **SQLAlchemy** and **PyMySQL**.

---

## ✨ Key Features

- 📦 **Containerized Orchestration:** Isolated Docker containers for database and ETL scripts using custom network bridging.
- 🧹 **Schema Normalization:** Standardizes raw header formats (trimming whitespaces, lowercase conversion, and replacing spaces with underscores).
- 🔤 **Robust Encoding Handling:** Handles non-UTF8 text formats safely using `latin1` fallback parsers.
- 🛡️ **URL-Safe Parsing:** Solves connection string URL-parsing collisions with complex database credentials.
- ⚡ **Automated DDL & Ingestion:** Leverages SQLAlchemy to infer column types automatically and map Pandas DataFrames to native MySQL schemas (`bigint`, `double`, `text`).

---

## ⚙️ Tech Stack & Architecture

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core ETL script execution and string processing |
| **Data Engine** | Pandas | High-performance DataFrame parsing and schema cleanup |
| **Database ORM** | SQLAlchemy / PyMySQL | Relational Database connection & SQL execution |
| **Database** | MySQL 8.0 | Relational storage layer hosted in Docker |
| **Containerization** | Docker / WSL2 | Container execution, isolated ports, and volume mapping |

---

## 🧮 Pipeline Architecture & Flow

```text
  [ Raw CSV File ] 
        │ (Latin1 Encoding)
        ▼
   [ Extract ] ─────► Read into Pandas DataFrame
        │
        ▼
 [ Transform ] ─────► Normalize Column Names (lowercase, trimmed, underscores)
        │
        ▼
    [ Load ] ────────► Stream via PyMySQL Engine
        │
        ▼
 [ MySQL Database ] ──► Schema TestDB (Table: kaggle_data)