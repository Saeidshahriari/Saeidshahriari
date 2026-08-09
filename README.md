# Hi there, I'm Saeid Shahriari 👋

> **Data & MLOps Engineer** | Master's Student in Applied Computer Science  
> Building resilient data pipelines, scalable stream-processing systems, and LLM-powered data extraction workflows.

---

## 🛠️ Core Stack & Tools

**Languages & Frameworks:**
`Python 3.12` `SQL` `PySpark` `PyFlink` `FastAPI` `Pydantic`

**Data & LLM Engineering:**
`Apache Kafka` `Apache Airflow` `dbt` `Gemini AI API` `OCRmyPDF / Tesseract`

**Databases & Infrastructure:**
`PostgreSQL (JSONB)` `ClickHouse` `Snowflake` `Docker Compose` `Alembic` `SQLAlchemy`

---

## 🚀 Key Architectural Projects

### 📄 Intelligent Document Extraction Pipeline *(Belgian Gazette Deeds)*
* **Focus:** Risk-first PDF ingestion, OCR, LLM extraction with Gemini 2.5 Flash, and relational PostgreSQL modeling.
* **Architecture Highlights:**
  * **Risk-First Prototyping:** Validated OCR → LLM JSON → Pydantic schema workflow before database design.
  * **Complex Entity Relational Mapping:** Handled multi-notice PDF complexity by decoupling `documents`, `deeds`, `companies`, and `party_roles`.
  * **Resilience & Idempotency:** Implemented SHA-256 file hashing for duplicate detection and exponential backoff retry logic (`tenacity`) for LLM rate-limits.
  * **Serving Layer:** Exposed clean REST endpoints via FastAPI for business decision-maker lookup and enterprise querying.

### ⚡ Real-Time CDC Streaming Platform
* **Focus:** Change Data Capture (CDC) pipeline for real-time analytics.
* **Tech:** Kafka | Flink SQL | Debezium | Redis | OpenSearch | Docker

### 🛡️ Privacy-Driven Streaming Data Pipeline
* **Focus:** Dynamic masking, HMAC tokenization, and GDPR-compliant sanitized schema generation.
* **Tech:** PostgreSQL | Python | Docker | Privacy Engineering

---

## 📈 Engineering Philosophy

* **Risk-First Development:** Tackle the hardest unknowns (data quality, extraction variance) before writing infrastructure code.
* **Data Integrity Over Volume:** Focus on schema validation, idempotency, and explicit error handling before scaling batch sizes.
* **Clear System Boundaries:** Keep API boundaries clean, avoiding heavy pipeline dependencies in lightweight serving containers.
