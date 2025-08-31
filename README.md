# 🧠 Cancer Detection ML App with Full DevOps Pipeline

This project demonstrates the complete DevOps lifecycle of deploying a machine learning-based cancer risk prediction app. Built using Flask (Python) and served through a responsive HTML/CSS/JavaScript frontend, the application is containerized, automated, and deployed using modern DevOps tools like Docker, Jenkins, and AWS.

---

## 📦 Features

- 🧠 **ML-Powered Risk Prediction** using Random Forest
- 🐍 **Flask Backend** serving predictions via `/predict` API
- 🌐 **Responsive Frontend** with dynamic AJAX interactions
- 🐳 **Dockerized** frontend and backend for isolated environments
- 🔁 **CI/CD Pipeline** using GitHub → Jenkins → DockerHub
- ☁️ **Cloud Deployment** on AWS EC2
- 🪵 **Log Automation** with AWS S3 backup via cron job

```
## 🗂️ Project Structure

final-devOps/
├── backend/
│ ├── app.py
│ ├── Cancer_Detection.pkl
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── index.html
│ ├── detection.html
│ ├── detection.js
│ └── styles.css
├── docker-compose.yml
├── backup_logs.sh

---
```
## 🚀 Getting Started

### 1. Clone the Repo

```
git clone https://github.com/yourusername/final-devOps.git
cd final-devOps
2. Run Locally with Docker Compose
docker-compose up --build
```
Visit: http://localhost:8080 (Frontend)

Backend API: http://localhost:5000/predict

🧪 ML Model
Trained using RandomForestClassifier on custom cancer dataset.

Features: age, gender, BMI, smoking, genetic risk, activity, alcohol intake, cancer history.

Stored as: Cancer_Detection.pkl

⚙️ CI/CD Pipeline
GitHub triggers Jenkins build on each push.

Jenkins builds Docker image of the backend.

Docker image pushed to DockerHub.

Optional: auto-pull and deploy to EC2.

☁️ Cloud Deployment on EC2
EC2 instance running Ubuntu 22.04

Docker & Docker Compose installed

Hosted on public IP: http://<EC2-IP>/

Deployed using:
```
docker-compose up -d
🪣 S3 Log Backup Automation
backup_logs.sh extracts container logs
```
Logs are uploaded to S3 bucket: final-devops-logs-backup

Scheduled via crontab to run daily at midnight:

cron
```
0 0 * * * /home/ubuntu/final-devOps/backup_logs.sh >> /home/ubuntu/cron.log 2>&1
```
📊 Summary
Phase	Task	Status
1	Dockerized Frontend + Backend	✅ Complete
2	CI/CD Pipeline (GitHub → Jenkins)	✅ Complete
3	EC2 Live Deployment	✅ Complete
4	Log Backup to AWS S3	✅ Complete

✨ Optional Future Upgrades
🔐 HTTPS via Nginx + Certbot

☁️ Centralized monitoring with AWS CloudWatch

🔄 Auto-deployment from Jenkins to EC2

🕵️ Load testing using Locust or k6

👨‍💻 Author
Muhammad Basit Khurshid
Bachelor of Information Technology
Punjab University, Lahore
📧 mbasitkhan10@gmail.com
