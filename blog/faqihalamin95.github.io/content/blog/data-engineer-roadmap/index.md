---
title: My Data Engineering Roadmap as a Data Science Student
summary: After sharing my motivation for pursuing Data Engineering, I wanted to put that passion into a structured plan. Something that connects what I learn in university, online courses, and real-world practice.
date: 2025-10-19
authors:
  - me
tags:
  - Roadmap
  - Data Engineer
  - Learning Journey
  - SQL
  - Python
cover:
  image: "cover.jpg"
image:
  filename: featured.jpg
  caption: "Image credit: Photo by [**Wes Hicks**](https://unsplash.com/@sickhews) on [**Unsplash**](https://unsplash.com)"
content_meta:
  trending: false
featured: true
---

 **After sharing my motivation for pursuing Data Engineering, I wanted to put that passion into a structured plan. Something that connects what I learn in university, online courses, and real-world practice.**

---

### Overview

I designed this roadmap to align with eight semesters of my Data Science degree, combining theory from coursework and technical depth from self-learning. Each semester focuses on a specific layer of data engineering, from local experimentation to production-grade cloud systems.

This roadmap isn’t just a checklist, it’s a direction map. Flexible enough to adapt as I grow, but clear enough to keep me focused.

As a Data Science student, my goal is to *build solid* ***foundations first***, ***automate second***, and ***scale last***.

---

### Roadmap Table

**Foundation (Phase 1-2)**

| Phase | Status | Main Focus | Learning Resources | Key Skill & Topics | Tools / Platform | Project / Portfolio Output |
| --- | --- | --- | --- | --- | --- | --- |
| 1\. Foundation Basics (2 months) | ✅ Completed | Python & SQL Fundamentals | Cisco - (Python Essentials 1, Linux Unhatched), Codecademy - Learn SQL, Codedex - Learn Git & Github | Basic statistics, Python basics, SQL fundamentals, intro to Git & Linux | Python, Jupyter Notebook, GitHub, Linux Shell, PostgreSQL/MySQL | **Project 1**: Basic Python scripting + simple SQL database & exploratory analysis |
| 2\. Local ETL & Modeling (2 months) | ⏳ In Progress | Databases & Local Data Handling | Databricks Academy (Data Modeling Strategies, Intro to Python for DS & DE, SQL Programming & Procedural Logic, Get Started with SQL Analytics & BI, Databricks SQL Performance Best Practices), pandas docs, PostgreSQL tutorial, MySQL docs, IBM: Linux Commands & Shell Scripting | CSV/JSON ingestion, Pandas ETL, Bash automation, ERD design, normalization, basic ETL patterns | PostgreSQL/MySQL, GitHub, Pandas & NumPy, Bash CLI | **Project 2:** Local ETL: ingest → clean → store data in SQL DB → export to CSV (with proper data modeling) |

---

**Cloud/Pipeline (Phase 3-5)**

| Phase | Status | Main Focus | Learning Resources | Key Skill & Topics | Tools / Platform | Project / Portfolio Output |
| --- | --- | --- | --- | --- | --- | --- |
| 3\. Cloud Foundations (4 months) |  | Cloud basics, Infrastructure setup, Containerization |  | IAM fundamentals, Object storage (S3/GCS), networking basics (VPC/Subnet), advanced Bash, Dockerizing environments, IaC fundamentals | AWS S3, IAM, Boto3, Bash, Docker, Terraform | **Project 3:** Automated data backup to cloud using Python/Bash (deploy via Docker container) |
| 4\. Serverless & IaC Pipelines (4 months parallel with phase 3) |  | Serverless Infrastructure & Basic Pipelines |  | Event-driven processing, Lambda functions, queue-based workflows, micro ETL orchestration, IaC deployment pipelines | AWS Lambda, SQS, Terraform, GitHub | **Project 4:** Serverless data pipeline deployed via Terraform |
| 5\. Big Data & Orchestration (5 months) |  | Big Data, Cloud ETL & Basic Streaming |  | Spark DataFrames, distributed processing, Glue ETL workflows, Redshift integration, dbt SQL modeling, Airflow DAG orchestration, data quality frameworks | Apache Spark (PySpark), AWS Glue, Redshift, Airflow/Step Functions, Kafka/Kinesis, dbt | **Project 5:** Cloud ETL — raw → Glue → Redshift/S3 + basic streaming ingestion + data quality checks |

---

**Advanced/Production (Phase 6-7)**

| Phase | Status | Main Focus | Learning Resources | Key Skill & Topics | Tools / Platform | Project / Portfolio Output |
| --- | --- | --- | --- | --- | --- | --- |
| 6\. DevOps & Production (4 months) |  | CI/CD, Observability & Container Orchestration |  | Infrastructure automation, secret management, GitHub Actions pipelines, test workflows, monitoring & logging, container orchestration (K8s) | Terraform, GitHub Actions, CloudWatch, Docker, Kubernetes | **Project 6:** Production-grade ETL with CI/CD, tests, monitoring, containerized deployment |
| 7\. Lakehouse & Capstone (8 months) |  | Lakehouse, Advanced Streaming & ML Integration |  | Delta Lake/Hudi, ACID ingestion, Spark optimization, incremental loads, real-time streaming (Flink/Spark Streaming), data governance, feature stores, ML pipeline integration | Databricks, Delta Lake, Flink/Spark Streaming, Great Expectations, MLflow, Terraform, Airflow, Power BI/Metabase | **Capstone:** Full data platform — ingestion → processing → catalog → quality → dashboard + ML pipeline |

---

### How I’ll Use This Roadmap

* **As a compass**, to keep me aligned with my long-term goal: becoming a professional Data Engineer.
    
* **As a progress tracker**, to document what I’ve learned and what still needs improvement.
    
* **As content inspiration**, for future blog posts and portfolio updates.
    

This roadmap isn’t final, it’s something I’ll refine every semester as I gain experience through university projects, certifications, and my ongoing work in the data industry.

---

### What’s Next

Phase 1 is complete.  
Phase 2 is now underway, focusing on **Local ETL & Data Modeling,** ingesting, cleaning, modeling, and storing data locally in a structured, reproducible way.

At the end of Phase 2, I’ll write a reflection post on what worked, what broke, and what I learned while moving from a simple pipeline to more structured local ETL workflows.

---

### **Roadmap Update Log**

**v2.1 — Phase 2 Learning Resources Update (December 2025)**

* Change and refine Phase 1 status and documentation.
    
* Added Phase 2 learning resources.
    
* Update on What’s Next section.
    

**v2.0 — Major Revision (December 2025)**

* Roadmap structure changed: semester-based → phase-based (7 phases).
    
* Cloud section updated: combined Cloud Foundations & Serverless Pipelines.
    
* Big Data phase revised: PySpark, dbt, and Airflow integrated into a single project.
    
* Added Workload Management & Burnout Prevention guidance.
    
* Capstone scope clarified: full data platform + ML integration.
    

**v1.2 — Tooling Update (November 2025)**

* Introduced Terraform basics for early IaC exposure.
    
* Added Docker containerization in Phase 3.
    

**v1.1 — Initial Structure (October 2025)**

* First version of the roadmap published.
    
* Added foundation milestones and basic Python/SQL projects.