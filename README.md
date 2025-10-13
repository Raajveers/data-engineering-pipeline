Advanced Data Pipeline Automation Project : CI/CD for Data Processing with Docker & Jenkins : Containerized Data Workflow Automation : 

I designed a CI/CD pipeline project to automate data processing using Python and Docker, and configured Jenkins for testing and deployment.
I also used Terraform to provision an S3 bucket in AWS.

I built a containerized data pipeline with Docker and Python, integrated Jenkins to run build and test stages using declarative pipelines.
I automated infrastructure provisioning with Terraform, managing state locally.
The pipeline runs unit tests, handles output validation, and pushes results to an AWS S3 bucket. Git and GitHub were used for full CI/CD version control.

# 🛠️ Data Engineering Pipeline with Docker, Jenkins & Terraform

This is a complete CI/CD-driven data pipeline project built using **Python**, **Docker**, **Jenkins**, and **Terraform** — designed to simulate a real-world data engineering scenario.

---

## 📌 Project Overview

- **Data generation and processing** using Python (pandas, numpy)
- **Containerized** using Docker
- **Test automation** using Pytest
- **CI/CD pipeline** implemented in Jenkins (build, test, run)
- **S3 bucket provisioning** via Terraform
- Code and infra fully version-controlled in GitHub

---

## 🧱 Folder Structure

```bash
data-engineering-pipeline/
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── s3_bucket.tf
├── scripts/
│   ├── __init__.py
│   ├── data_processing.py
│   └── test_data_processing.py
├── .gitignore
└── README.md


Step 1: Build Docker Image
  docker build -t data-engineering-pipeline .

Step 2: Run Container
  docker run --rm data-engineering-pipeline

Step 3: Run Tests
  pytest scripts/test_data_processing.py

Sample Output :
  ✅ Data saved to: output/data.csv
   ID  Value
    0   1     42
    1   2     56
    2   3     18
      ...

Technologies Used : - 

      Python 3.10
      Docker
      Jenkins
      Terraform
      AWS S3
      Pytest

Terraform S3 Module :
  s3_bucket.tf:

provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "data_pipeline_bucket" {
  bucket = "data-pipeline-bucket-raajveer-01"
  acl    = "private"
}


.gitignore :
    __pycache__/
    *.pyc
    venv/
    .terraform/
    .terraform.lock.hcl
    terraform.tfstate
    terraform.tfstate.backup
    output/

Future Improvements : 

    Add logging and error handling
    Trigger Jenkins build on GitHub webhook
    Add email/slack notifications in Jenkins
    Push data to S3 automatically

Final Status : 
✅ Dockerized ✅ Jenkins ✅ Pytest ✅ Terraform ✅ GitHub

        Author : 
    Raajveer Sutar ❤️

