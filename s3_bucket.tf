provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "data_pipeline_bucket" {
  bucket = "data-pipeline-bucket-raajveer-01"  # Must be globally unique
  acl    = "private"

  versioning {
    enabled = true
  }

  tags = {
    Name        = "Data Engineering Pipeline Bucket"
    Environment = "Dev"
  }
}

