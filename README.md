# qa-demo-project
# QA Automation for VMS Backend API

A demo automation framework built for testing the backend APIs of a Visitor Management System (VMS).  
It covers authentication, user registration, login, token validation, and edge-case handling (like 429 rate limiting).

---

## 🚀 Features

- ✅ Automated API test cases using `pytest`
- 🔄 Retry mechanism for 429 (Too Many Requests)
- 🔐 Token-based authentication testing
- 📄 Session-level setup and teardown using fixtures
- 📂 Credential handling with JSON persistence
- 📊 Integration-ready with Jenkins for CI/CD

---

## 🛠 Tech Stack

- **Language/Framework**: Python 3.10, Pytest
- **Tools**: Postman, Git, PyCharm, Jenkins
- **Database**: SQLite (for dev), PostgreSQL (in prod)
- **Libraries**: `requests`, `pytest`, `json`, `time`, `os`

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/example-user/qa-demo-project.git
cd qa-demo-project
