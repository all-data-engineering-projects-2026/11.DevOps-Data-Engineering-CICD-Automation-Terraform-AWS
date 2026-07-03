# DevOps Automation for Data Engineering using Terraform on AWS

**Infrastructure as Code (IaC) + Full CI/CD Pipeline for Modern Data Platforms — Complete Live Evidence**

This project demonstrates **production-grade DevOps practices** for Data Engineering on AWS using **Terraform** and **GitHub Actions**. It builds a complete, automated data foundation with S3 Data Lake, Glue Catalog, Scheduled Crawler, and a robust multi-stage CI/CD pipeline.

---

## 🚀 Key Achievement

Successfully delivered a fully automated data ingestion platform with:

- **Terraform IaC** provisioning S3 + Glue Catalog + Crawler with best practices
- **GitHub Actions CI/CD** (Security → Test → Validate → Plan → Deploy)
- **End-to-end verification** — Athena successfully querying 10,000 rows from the Glue Catalog
- All components version-controlled, tested, and deployed through automated pipelines

---

## 🏗️ Architecture

**Flow:**
```
Developer (Terraform + Python Code)
        ↓
GitHub Actions CI/CD Pipeline
        ↓
Terraform Apply → AWS Resources
        ↓
S3 Raw Data → Glue Crawler → Glue Catalog → Athena (Queryable)
```

**Core Components:**
- S3 Data Lake (with AES-256 encryption)
- Glue Data Catalog + Daily Scheduled Crawler
- Dedicated IAM Role (least privilege)
- Full CI/CD with security scanning and testing

---

## 🛠️ Technology Stack

| Category                  | Technology                          | Purpose |
|---------------------------|-------------------------------------|--------|
| **Infrastructure as Code**| Terraform v1.15.7                   | Declarative AWS provisioning |
| **Cloud Platform**        | AWS (ap-south-1)                    | S3, Glue, IAM |
| **Data Catalog**          | AWS Glue Data Catalog + Crawler     | Automated metadata & schema discovery |
| **CI/CD**                 | GitHub Actions                      | Security, Testing, Deployment pipeline |
| **Testing**               | pytest + pytest-cov                 | Unit tests + coverage reporting |
| **Security**              | Bandit + Safety                     | Static analysis & dependency scanning |
| **Query Engine**          | Amazon Athena                       | Serverless SQL on Glue Catalog |

---

## 📁 Project Structure

```
11.DevOps_Automation_DE_Terraform_AWS/
├── scripts/
│   └── generate_sample_data.py          # Synthetic temperature data generator
├── tests/
│   └── test_generate_sample_data.py     # 7 pytest tests (100% passing)
├── terraform/
│   ├── main.tf                          # S3 + Glue + IAM + encryption + safe destroy logic
│   ├── variables.tf
│   ├── outputs.tf
│   └── provider.tf
├── .github/workflows/
│   └── deploy.yml                       # Full CI/CD pipeline
├── data/
│   └── temperature_data.csv             # 10,000 rows sample data
└── requirements.txt
```

---

## 🔧 Key Implementation Highlights

### Terraform Best Practices
- `create_before_destroy` lifecycle on critical resources
- `null_resource` + `local-exec` for safe S3 bucket emptying before destruction
- AES-256 server-side encryption enabled by default
- Dedicated IAM role with `AWSGlueServiceRole` + `AmazonS3FullAccess`

### CI/CD Pipeline (GitHub Actions)
- **Security Scan**: Bandit + Safety
- **Test**: pytest with coverage (artifact uploaded)
- **Validate**: `terraform validate`
- **Plan**: `terraform plan` (tfplan artifact for review)
- **Deploy**: Only runs on `main` with environment protection

### Data & Testing
- Realistic temperature data for 5 global cities
- Timestamps spread over 365 days
- Comprehensive pytest suite covering edge cases and file permissions

---

## 📸 Live Implementation Evidence

Complete documentation with **17 figures** (screenshots) is available in:

📄 **[Terraform_DevOps_Project_DE_Notes.pdf](Terraform_DevOps_Data_Engineering_Final_Notes.docx)**

**Key Evidence:**
- Successful `terraform apply` (5 resources created)
- S3 bucket with `temperature_data.csv`
- Glue Crawler running with successful previous runs
- Glue Database + Table automatically created
- IAM Role correctly configured
- **Athena query returning 10,000 rows** successfully
- Multiple successful GitHub Actions workflow runs

---

## 🧠 Skills Demonstrated

- Infrastructure as Code with Terraform (S3, Glue Catalog, Crawler, IAM)
- AWS Data Engineering services (Glue + S3 Data Lake)
- Production CI/CD pipeline design (GitHub Actions — security-first)
- Python testing best practices (pytest + coverage)
- Security automation in pipelines (Bandit, Safety)
- Terraform state management & safe destruction patterns
- End-to-end Data Engineering platform automation on AWS

---

## ▶️ How to Run

### Local Development
```bash
# Generate sample data
python scripts/generate_sample_data.py

# Run tests
PYTHONPATH=. pytest tests/ -v --cov=scripts
```

### Terraform Deployment
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

### CI/CD
Push to `dev` or `main` branch. GitHub Actions will automatically run the full pipeline.

---

## 📌 Notes

- **Region**: ap-south-1 (default)
- **S3 Bucket**: `dml-temperature-analysis-him-raw-data`
- **Glue Crawler Schedule**: Daily at 1:00 AM UTC
- This project follows modern **DevOps + Data Engineering** best practices and is production-ready

---

**Author:** Himanshu  
**Date:** July 2026  
**Portfolio Project**

For complete technical documentation with all screenshots, code explanations, and live evidence, refer to:

📄 **Terraform_DevOps_Project_DE_Notes.pdf**