# SIH1652-DocVerification.
Smart India Hackathon 2025 Project: Document Verification using AI and OCR.
SIH1652 – Document Verification using AI & OCR
📌 Problem Statement
Recruitment and Assessment Centre (RAC) under DRDO requires a system to extract and verify information from semi-categorized documents (certificates, mark sheets, caste/EWS/PwD certificates, etc.).
Currently, the process is manual and time-consuming. Documents may be in image/PDF format and in multiple languages.
The goal is to build an AI-powered Intelligent Document Processing (IDP) system that:
Extracts details (using OCR & NLP).
Verifies against applicant biodata.
Flags mismatches instantly.
Provides fast and reliable results (≤ 3 seconds per document).

🎯 Objectives
Automate document verification.
Ensure Three Sigma accuracy in data extraction.
Support documents in multiple languages.
Build a dashboard to visualize verification results.

🛠️ Tech Stack
Python
OCR → Tesseract / EasyOCR
NLP → spaCy / Transformers
Deep Learning → PyTorch / TensorFlow
Data Handling → Pandas, OpenCV
Dashboard → Streamlit / Flask
Database → SQLite / PostgreSQL

📂 Repository Structure
/data         → Sample documents
/code         → Main Python scripts
/models       → Trained ML models
/dashboard    → Streamlit/Flask dashboard files
/docs         → Reports, PPT, notes

🚀 How to Run
Clone the repository:
git clone https://github.com/sharmila628/SIH1652-DocVerification.git
cd SIH1652-DocVerification
Install dependencies:
pip install -r requirements.txt
Run the OCR extraction:
python code/extract.py
Start the dashboard:
streamlit run dashboard/app.py

📊 Expected Outcome
AI verifies applicant documents automatically.
Mismatch alerts shown in real-time.
Admins get a dashboard with analytics and verification results.
