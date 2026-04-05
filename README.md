# 🔐 AWS Security Misconfiguration Scanner

A Python-based cloud security tool that scans AWS resources for common misconfigurations such as publicly accessible S3 buckets and insecure EC2 security group rules.

---

## 🚀 Features

* 🔍 Detects **public S3 buckets** (ACL-based exposure)
* 🌐 Identifies **security groups open to the internet** (0.0.0.0/0)
* 📊 Provides a **scan summary** with issue counts
* ⚡ Lightweight and easy to run using Python and boto3

---

## 🛠️ Tech Stack

* **Python**
* **AWS (S3, EC2, IAM)**
* **boto3 (AWS SDK for Python)**

---

## 📂 Project Structure

```
aws-security-scanner
│
├── scanner.py                # Main controller
├── s3_check.py               # S3 security checks
├── security_group_check.py   # EC2 security checks
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Setup & Installation

1. Clone the repository:

```
git clone https://github.com/your-username/aws-security-scanner.git
cd aws-security-scanner
```

2. Create virtual environment (recommended):

```
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Configure AWS credentials:

```
aws configure
```

---

## ▶️ How to Run

```
python scanner.py
```

---

## 📊 Example Output

```
AWS Security Misconfiguration Scanner
--------------------------------------

Checking S3 buckets...

Checking Security Groups...

Scan Summary
-------------
S3 Issues: 0
Security Group Issues: 1
```

---

## 🔍 Security Checks Implemented

### 1. S3 Bucket Exposure

* Detects publicly accessible buckets via ACL permissions

### 2. Security Group Exposure

* Detects open ports accessible from anywhere (`0.0.0.0/0`)

---

## 📌 Future Improvements

* Detect **bucket policy-based public access**
* Add **JSON report export**
* Add **CLI arguments for selective scanning**
* Integrate **real-time alerts**

---

## 💡 Learning Outcomes

* Hands-on experience with **AWS cloud security**
* Understanding of **misconfiguration vulnerabilities**
* Practical use of **boto3 for automation**
* Building modular and scalable Python projects

---

## 📎 Author

**Neha Merin**

---

## ⭐ Acknowledgements

This project was built as part of hands-on learning in **Cloud Computing and Cybersecurity**.
