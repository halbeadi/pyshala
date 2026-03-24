# 🧪 PyShala – Secure Python Learning Platform

An interactive platform for learning Python with a focus on **secure code execution and controlled environments**.

---

## 🚀 Overview

PyShala allows users to write and execute Python code in a structured learning environment with built-in validation and testing.

The platform is designed with **security-first principles**, ensuring safe execution of user-submitted code.

---

## 🛡️ Security Features (🔥 MOST IMPORTANT)

* Sandbox-based code execution
* Input validation for user-submitted code
* Restricted system access
* Isolation of execution environment
* Protection against malicious scripts

---

## 🧠 Core Features

* Interactive coding environment (Monaco Editor)
* YAML-based modular lesson system ([PyPI][1])
* Automated test case validation
* Structured learning flow (Modules → Lessons)

---

## ⚠️ Security Testing

The platform has been tested against:

* SQL Injection attempts
* Cross-Site Scripting (XSS)
* Malicious Python execution
* Infinite loop / resource exhaustion attacks
* Unauthorized file/system access

---

## 🧪 Example Threat Scenarios

```python
# Infinite loop attack
while True:
    pass
```

```python
# System access attempt
import os
os.system("ls")
```

👉 These are handled using sandbox restrictions and execution control.

---

## ⚙️ Tech Stack

* Python (Backend + Logic)
* Reflex (Frontend + Backend Framework)
* Monaco Editor (Code Editor)
* YAML (Lesson Structure)

---

## 🚀 Future Enhancements

* Role-Based Access Control (RBAC)
* Secure Authentication (JWT/OAuth)
* Activity Logging & Monitoring
* AWS Cloud Deployment with security best practices

---

## 📸 Screenshots (ADD THIS)

(Add images here — VERY IMPORTANT)

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/halbeadi/pyshala.git
cd pyshala
pip install -r requirements.txt
```

---

## 📌 Why This Project Matters

This project demonstrates:

* Secure system design
* Safe execution of untrusted code
* Practical application of security principles

---

⭐ Designed with a focus on **Cloud & Application Security**

[1]: https://pypi.org/project/pyshala/?utm_source=chatgpt.com "pyshala · PyPI"
