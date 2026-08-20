# Hi there, I'm Saeid Shahriari 👋

> **Data & MLOps Engineer** |
> Building resilient data pipelines, scalable stream-processing systems, and
> secured lakehouse platforms where data quality is enforced, not assumed.

---

### 🛠️ Core Technologies & Tools

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-025E8D?style=for-the-badge&logo=postgresql&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

**Data Engineering & Streaming**

![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)
![Apache Flink](https://img.shields.io/badge/Apache_Flink-E6526F?style=for-the-badge&logo=apacheflink&logoColor=white)
![Debezium](https://img.shields.io/badge/Debezium_CDC-4000BF?style=for-the-badge&logo=redhat&logoColor=white)
![Parquet](https://img.shields.io/badge/Parquet-50ABF1?style=for-the-badge&logo=apacheparquet&logoColor=white)

**Storage & Query**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![OpenSearch](https://img.shields.io/badge/OpenSearch-005EB8?style=for-the-badge&logo=opensearch&logoColor=white)

**MLOps & Security**

![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![HashiCorp Vault](https://img.shields.io/badge/Vault-FFEC6E?style=for-the-badge&logo=vault&logoColor=black)
![OWASP](https://img.shields.io/badge/OWASP_ZAP-000000?style=for-the-badge&logo=owasp&logoColor=white)

**Platform & Serving**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

## 🚀 Key Architectural Projects

### ⚡ [ETRM Data Platform](https://github.com/Saeidshahriari/etrm-data-platform) *(Energy Trading & Risk Management)*

A secured medallion lakehouse for European energy trading, with seven security
layers and an unsupervised market-abuse surveillance model.

* **Tech:** Airflow 3 | Spark 4 | PostgreSQL 16 | Vault | scikit-learn | MLflow | DuckDB | Streamlit | Docker
* **Architecture Highlights:**
  * **Medallion lakehouse:** Bronze (raw JSON) to Silver (typed, deduplicated) to Gold (PnL, counterparty exposure, portfolio summary), all in Parquet.
  * **MLSecOps, layers A to G:** gitleaks, Bandit, Semgrep, pip-audit, Trivy, Hadolint, Checkov and OWASP ZAP in CI, plus a data-poisoning gate that runs on live data inside the pipeline.
  * **Data as an attack surface:** every incoming string is scanned for SQL, script, path-traversal and **prompt injection**, because the data is later shown to an LLM agent.
  * **Quarantine, do not crash:** bad rows are set aside rather than failing the run, so a single poisoned value cannot become a denial-of-service.
  * **REMIT surveillance model:** Isolation Forest, unsupervised because real market abuse is rare and unlabelled. 3/3 planted abuse patterns detected, 5% false-positive rate, and every alert carries a human-readable reason.
  * **Found a real bug in production data:** the poisoning gate caught an ingestion filter that was fetching grid load in MW instead of price in EUR/MWh. Code review had missed it.

### 📄 Intelligent Document Extraction Pipeline *(Belgian Gazette Deeds)*

* **Focus:** Risk-first PDF ingestion, OCR, LLM extraction with Gemini 2.5 Flash, and relational PostgreSQL modeling.
* **Architecture Highlights:**
  * **Risk-First Prototyping:** Validated OCR to LLM JSON to Pydantic schema workflow before database design.
  * **Complex Entity Relational Mapping:** Handled multi-notice PDF complexity by decoupling `documents`, `deeds`, `companies`, and `party_roles`.
  * **Resilience & Idempotency:** SHA-256 file hashing for duplicate detection, and exponential backoff retry logic (`tenacity`) for LLM rate limits.
  * **Serving Layer:** Clean REST endpoints via FastAPI for business decision-maker lookup and enterprise querying.

### 🔄 Real-Time CDC Streaming Platform

* **Focus:** Change Data Capture pipeline for real-time analytics.
* **Tech:** Kafka | Flink SQL | Debezium | Redis | OpenSearch | Docker

### 🛡️ Privacy-Driven Streaming Data Pipeline

* **Focus:** Dynamic masking, HMAC tokenization, and GDPR-compliant sanitized schema generation.
* **Tech:** PostgreSQL | Python | Docker | Privacy Engineering

---

## 📈 Engineering Philosophy

* **Risk-First Development:** Tackle the hardest unknowns, such as data quality and extraction variance, before writing infrastructure code.
* **Data Integrity Over Volume:** Schema validation, idempotency and explicit error handling come before scaling batch sizes.
* **Trust Nothing Upstream:** Treat incoming data as an attack surface, not just as input. Validate ranges, scan for injection, and quarantine instead of crashing.
* **Root Cause Over Workaround:** Verify each fix before moving to the next step. A symptom that disappears is not the same as a cause that is understood.
* **Clear System Boundaries:** Keep API boundaries clean, avoiding heavy pipeline dependencies in lightweight serving containers.

---

## 📫 Get in touch

![Location](https://img.shields.io/badge/Brussels-Belgium-000000?style=flat-square&logo=googlemaps&logoColor=white)
![Open to](https://img.shields.io/badge/open_to-Data_Engineering_%2F_MLOps-success?style=flat-square)

---

## 📈 Live System Status

![Dynamic Profile Status](./status.svg)
