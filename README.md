🔐 Secure Anonymous Evidence Vault

A secure, integrity-preserving digital evidence storage system designed for anonymous submissions and forensic verification.

📌 Overview

The Secure Anonymous Evidence Vault is a cybersecurity-focused project(MVP) that enables users to securely upload digital evidence, store it in encrypted form, and later verify its integrity using cryptographic hashing.

The system is designed with forensic soundness, confidentiality, and tamper detection in mind — aligning with real-world digital forensics and incident response workflows.

🎯 Problem Statement

Digital evidence is often:

Altered intentionally or unintentionally

Stored without proper integrity verification

Difficult to validate during investigations

This project addresses these challenges by implementing:

Encryption at rest

Hash-based integrity verification

Case-ID–based evidence tracking

🛡️ Key Security Features

🔑 Encryption at Rest
Evidence files are encrypted before storage to prevent unauthorized access.

🧾 Cryptographic Hashing (SHA-256)
Each file is hashed at upload time to establish a forensic integrity baseline.

🧬 Tamper Detection
Any modification to stored evidence is detected during verification.

🆔 Unique Case ID Generation
Each submission is assigned a UUID for traceability without revealing identity.

🗃️ Forensic Metadata Logging
Hash values and storage paths are recorded securely in a database.

🧠 System Architecture
User Upload
   │
   ▼
[ Flask Web App ]
   │
   ├── Generate SHA-256 Hash
   ├── Encrypt Evidence
   ├── Assign Case ID
   ▼
[ Encrypted Vault Storage ]
   │
   ▼
[ SQLite Evidence Database ]

🧪 Evidence Verification Flow

Investigator provides a Case ID

Encrypted evidence is retrieved

Hash is recalculated

Hash is compared with the original stored hash

System reports:

✅ Integrity Verified

⚠️ Evidence Tampered

🧰 Tech Stack
Component	   Technology
Backend        Python (Flask)
Encryption	   Cryptography
Hashing        SHA-256
Database       SQLite
Frontend       HTML
Platform       Linux (Localhost)

🚀 How to Run Locally

1️⃣ Clone the repository
git clone https://github.com/your-username/secure-anonymous-evidence-vault.git
cd secure-anonymous-evidence-vault

2️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python3 app.py

Visit:
👉 http://127.0.0.1:5000
🔍 Verify Evidence Integrity
python3 verify.py <CASE_ID>

⚠️ Ethical & Legal Disclaimer

This project is developed strictly for educational and ethical cybersecurity purposes, including:

Digital forensics learning

Secure system design

Evidence handling simulation

⚠️ Do NOT use this system for illegal surveillance or unauthorized data collection.
