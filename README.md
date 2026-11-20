# Terraform Azure RAG Platform

Enterprise-style Retrieval Augmented Generation (RAG) platform built on Microsoft Azure using Azure OpenAI, Azure AI Search, LangChain, and Terraform.

The project demonstrates how platform and infrastructure engineers can deploy and operate a production-style knowledge assistant that retrieves information from enterprise documentation before generating responses with a Large Language Model (LLM).

---

## Why This Project?

Modern AI Platform Engineering teams are responsible for more than infrastructure provisioning.

A production AI platform typically requires:

- Enterprise Search
- Retrieval Augmented Generation (RAG)
- Large Language Model (LLM) Integration
- Observability
- Cost Monitoring
- Governance
- Operational Runbooks

This project demonstrates how Azure OpenAI and Azure AI Search can be combined to build an Engineering Knowledge Assistant capable of answering questions from enterprise operational documentation.

---

## Project Goal

Build an Engineering Knowledge Assistant that can answer questions from operational and platform documents such as:

- SVA Installation Guide
- Platform Operations Runbook
- Platform Troubleshooting Guide
- Platform Upgrade Procedure
- Infrastructure Architecture Standards
- AI Platform Deployment Standards

Instead of relying solely on LLM knowledge, the solution retrieves relevant enterprise documents and uses them to generate grounded responses.

---

## Architecture

```text
Enterprise Documents
        ↓
Azure Storage Account
        ↓
Azure AI Search
        ↓
LangChain Retriever
        ↓
Azure OpenAI
        ↓
Engineering Knowledge Assistant
```

---

## Technologies

### Infrastructure

- Terraform
- Microsoft Azure
- Azure Resource Groups
- Azure Storage Account

### AI Services

- Azure OpenAI
- Azure AI Search
- Embedding Models
- GPT Models

### Application Layer

- Python
- LangChain
- REST API

### Observability

- Application Metrics
- Retrieval Metrics
- Token Usage Metrics
- Latency Monitoring

---

## Repository Structure

```text
terraform-azure-rag-platform/
│
├── terraform/
│   ├── providers.tf
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars
│
├── app/
│   ├── api/
│   ├── rag/
│   └── requirements.txt
│
├── documents/
│   └── .gitkeep
│
├── architecture/
│   └── architecture.png
│
└── README.md
```

---

## Terraform Resources

The initial Terraform deployment provisions:

### Resource Group

Container for all Azure resources.

### Storage Account

Used for enterprise document storage.

### Azure AI Search

Provides:

- Vector Search
- Semantic Search
- Retrieval Layer
- Document Indexing

### Azure OpenAI

Provides:

- Embedding Models
- LLM Inference Endpoint
- Response Generation

---

## RAG Workflow

### Document Ingestion

```text
Enterprise Documents
        ↓
Text Extraction
        ↓
Chunking
        ↓
Embeddings Generation
        ↓
Azure AI Search Index
```

### Question Answering

```text
User Question
        ↓
Retriever
        ↓
Relevant Chunks
        ↓
Azure OpenAI
        ↓
Grounded Response
```

---

## Example Enterprise Use Cases

Example questions:

```text
What are the prerequisites for SVA installation?

Which ports must be opened before deployment?

How do I validate a successful installation?

What is the recommended upgrade procedure?

What post-installation checks should be performed?

How do I troubleshoot installation failures?

What are the rollback steps during an upgrade?
```

---

## Observability

This project focuses on platform-level observability for RAG workloads.

### Retrieval Metrics

- Search Latency
- Retrieval Success Rate
- Empty Retrieval Count
- Retrieved Chunk Count
- Search Request Count

### LLM Metrics

- Prompt Tokens
- Completion Tokens
- Total Tokens
- Request Count
- LLM Response Latency

### Platform Metrics

- End-to-End Response Latency
- Error Rate
- Requests per Second
- Cost Estimation
- Success Rate

---

## Learning Objectives

This project helps develop hands-on experience with:

- Retrieval Augmented Generation (RAG)
- Azure OpenAI
- Azure AI Search
- LangChain
- Embeddings
- Vector Search
- Enterprise Knowledge Assistants
- AI Platform Engineering
- LLM Observability
- Infrastructure as Code (Terraform)

---

## Roadmap

### Phase 1 - Infrastructure

- Terraform deployment
- Azure OpenAI
- Azure AI Search
- Storage Account

### Phase 2 - Knowledge Ingestion

- Document Upload
- Search Index Creation
- Embedding Generation
- Retrieval Testing

### Phase 3 - RAG Application

- LangChain Integration
- Retriever Implementation
- Source Citations
- Chat Interface

### Phase 4 - Observability

- Search Latency Monitoring
- OpenAI Latency Monitoring
- Token Usage Tracking
- Cost Monitoring
- End-to-End Response Metrics

### Phase 5 - Production Readiness

- AKS Deployment
- Containerization
- CI/CD Pipeline
- Authentication
- Production Monitoring

---

## Future Enhancements

- Hybrid Search
- Graph RAG
- Multi-Document Knowledge Base
- AI Agent Integration
- AKS Deployment
- Prometheus and Grafana Dashboards
- Cost Analytics Dashboard
- Enterprise Authentication

---

## Status

🚧 Work in Progress

Current Phase:

```text
Terraform
    ↓
Azure OpenAI
    ↓
Azure AI Search
```

Upcoming Phase:

```text
Document Ingestion
    ↓
LangChain
    ↓
RAG Chatbot
```

---

## Why This Matters for AI Platform Engineers

Modern AI Platform Engineering roles increasingly require experience with:

- RAG Architectures
- Enterprise Search Platforms
- LLM Integration
- Inference Endpoints
- Observability
- Governance
- Cost Optimization

This project focuses on those platform-engineering capabilities rather than only deploying infrastructure.
