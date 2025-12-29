# Self-Healing Backend System

An AI-powered backend system that continuously monitors service health
and system metrics, diagnoses failures, and autonomously triggers
recovery actions using an LLM-style decision agent.

## Features
- Health monitoring
- CPU & memory metrics
- LLM-powered decision engine
- Automatic recovery actions
- Structured logging
- Dockerized deployment (design)

## Architecture
Service → Monitor → LLM Decision Engine → Recovery Engine

## Run Locally

```bash
uvicorn app.main:app --reload
python app/monitor.py
```

## Docker (Optional)
```bash
docker build -t self-healing-backend .
docker run -p 8000:8000 self-healing-backend
```

## Why This Project

This project demonstrates reliability engineering, observability,
and AI-driven decision-making in backend systems.