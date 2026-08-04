# 🏥 Health Navigator AI

An AI-powered healthcare assistant built with **FastAPI, PostgreSQL, and Large Language Models (LLMs)**. The project combines healthcare knowledge with modern AI engineering to provide educational health conversations, symptom assessment, and medical report management.


---

# Overview

Health Navigator AI is a healthcare-focused AI application designed to help users understand health-related information through natural language interactions.

The project demonstrates production-style backend development practices including secure authentication, database design, API development, AI integration, and modular software architecture.

The goal is to explore the intersection of **healthcare and artificial intelligence** by building a scalable AI assistant platform.

---

# Features

## 🔐 Authentication & Security

* User registration and login
* JWT-based authentication
* Protected API routes
* Password hashing using bcrypt
* User-specific data access control

---

## 💬 AI Health Conversations

* AI-powered healthcare conversations
* Persistent conversation history
* User message and AI response storage
* Medical-focused system prompt
* Groq LLM integration

Conversation flow:

```
User
 ↓
FastAPI API
 ↓
Conversation Service
 ↓
Groq LLM
 ↓
AI Response
 ↓
Database Storage
```

---

## 🩺 Symptom Assessment

* Users can submit symptoms and basic information
* AI provides educational health guidance
* Helps users understand possible explanations and precautions
* Encourages professional medical consultation when required

> Disclaimer: This system provides educational information only and does not replace professional medical advice.

---

## 📄 Medical Report Upload

* Upload medical documents
* Store uploaded files
* Track report metadata in PostgreSQL
* Associate reports with authenticated users

Future improvements:

* PDF text extraction
* Medical document analysis
* Retrieval-Augmented Generation (RAG)

---

# Tech Stack

## Backend

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic

## Authentication

* JWT Authentication
* bcrypt Password Hashing

## Artificial Intelligence

* Groq LLM API
* Large Language Models
* Future Agentic AI workflows
* Future RAG pipeline

## Development Tools

 Git & GitHub
 Swagger / OpenAPI Documentation
 Pytest
 Postman(API testing)
 Postman (API testing)

---

# Project Architecture

The application follows a modular FastAPI architecture with separation of concerns.

```
app/
│
├── api/              # API endpoints and request handling
│
├── auth/             # Authentication, JWT, and password security
│
├── core/             # Application configuration and settings
│
├── database/         # Database connection and session management
│
├── models/           # SQLAlchemy database models
│
├── schemas/          # Pydantic request and response schemas
│
├── services/         # Business logic and external integrations
│
├── agents/           # AI agent modules (future expansion)
│
└── rag/              # Retrieval-Augmented Generation modules (future expansion)

tests/                # Automated tests
```

## Architecture Approach

```
API Layer
    ↓
Service Layer
    ↓
Database Layer
```

* **API Layer:** Handles HTTP requests, validation, and responses.
* **Service Layer:** Contains application business logic.
* **Database Layer:** Handles persistence using PostgreSQL and SQLAlchemy.
* **Authentication Layer:** Provides secure user access with JWT and password hashing.
* **AI Layer:** Handles integration with Large Language Models.

---

# API Documentation

FastAPI provides interactive Swagger documentation.

Available APIs:

## Authentication

```
POST /auth/signup
POST /auth/login
GET /auth/me
```

## Conversations

```
POST /conversations
GET /conversations
```

## Messages

```
POST /conversations/{conversation_id}/messages
GET /conversations/{conversation_id}/messages
```

## Symptom Assessment

```
POST /symptom-assessment
```

## Medical Reports

```
POST /reports/upload
```

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/noorfatima1028/health-navigator-ai.git

cd health-navigator-ai
```

---

## Create Virtual Environment

```bash
python -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```
DATABASE_URL=
SECRET_KEY=
GROQ_API_KEY=
```

---

## Database Migration

Run:

```bash
alembic upgrade head
```

---

## Start Application

```bash
uvicorn app.main:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

---

# Testing

Current tests include:

* Database connection tests
* Password hashing tests
* LLM integration tests

Future API tests will cover:

* Authentication endpoints
* Conversation APIs
* Message APIs
* Medical report uploads
* Symptom assessment

---

# Future Roadmap

* [ ] Complete API test coverage
* [ ] Medical PDF text extraction
* [ ] Retrieval-Augmented Generation (RAG)
* [ ] AI healthcare agents
* [ ] Docker containerization
* [ ] AWS cloud deployment
* [ ] CI/CD pipeline

---

# Purpose

This project represents my journey of combining healthcare knowledge with backend engineering and artificial intelligence to build practical healthcare AI solutions.

---

# Disclaimer

Health Navigator AI provides educational health information only.

It is not intended to diagnose conditions, prescribe treatments, or replace consultation with qualified healthcare professionals.
