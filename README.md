# 🚑 Self-Healing Backend System

An AI-assisted backend system that continuously monitors service health
and system metrics, detects anomalies, and **automatically triggers
recovery actions without human intervention**.

This project demonstrates how **autonomous systems and LLM-style reasoning**
can be applied to backend reliability engineering.

---

## 🎯 Problem Statement

Traditional backend systems:
- Detect failures
- Raise alerts
- Depend on human operators to fix issues

This leads to:
- Delayed recovery
- Increased downtime
- Operational overhead

The **Self-Healing Backend System** solves this by introducing an
**intelligent recovery loop** that can detect, diagnose, and fix
issues on its own.

---

## ✨ Key Features

- 📡 **Health Monitoring** (Service availability)
- 📊 **System Metrics Collection** (CPU & Memory)
- 🧠 **LLM-Style Decision Engine**
- 🚑 **Automated Recovery Actions**
- 📝 **Structured Logging**
- 🐳 **Dockerized Design (Optional)**

---

## 🏗️ High-Level Architecture

Service Health & Metrics
↓
Monitoring Engine
↓
Decision Engine (LLM-style)
↓
Recovery Engine
↓
Self-Healing Action


---

## 🧪 Example Scenario

###  Detected State
Service Status: UP
Memory Usage: 91%
CPU Usage: 20%

### AI Decision
Action: Clear Cache
Reason: Memory usage is critically high

### Result
Recovery executed automatically.
The system continuously monitors and re-evaluates the service after recovery.

---

## 🧠 How It Works

1. The backend exposes a `/health` endpoint
2. A monitoring process collects:
   - Service status
   - CPU usage
   - Memory usage
3. The decision engine analyzes metrics
4. Root cause is inferred using AI-style logic
5. A recovery action is executed
6. The event is logged for observability

---

## 🛠️ Tech Stack

- Backend - FastAPI 
- Monitoring - `psutil` 
- Decision Logic - LLM-style agent 
- Automation - Python 
- Logging File - based logs 
- DevOps - Docker  

---

## ▶️ Running Locally

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
### 2️⃣ Start Backend Service
```bash
uvicorn app.main:app --reload
Verify health:
http://127.0.0.1:8000/health
```
### 3️⃣ Start Monitoring Agent
```
python app/monitor.py
```
The system will begin monitoring and automatically trigger recovery
actions when anomalies are detected.

## 📈 Why This Project
Most backend systems:
- Alert humans when something breaks
This system:
- Fixes itself
It demonstrates:
- Reliability engineering
- Autonomous systems
- AI-driven decision making
- Production-style backend design

## 🚀 Future Enhancements
- Real LLM integration for richer reasoning
- Kubernetes health hooks
- Multi-service self-healing
- Predictive anomaly detection
- Persistent metrics storage

## 👤 Author
Chirag Guruswamy
