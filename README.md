# 🚀 Enterprise Azure Native AI Processing Platform

> **Enterprise-grade AI-powered document intelligence platform built entirely on Microsoft Azure.**

![Azure](https://img.shields.io/badge/Azure-Cloud-blue?style=for-the-badge\&logo=microsoftazure)
![Python](https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge\&logo=python)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge\&logo=docker)
![Flask](https://img.shields.io/badge/Flask-Microservices-black?style=for-the-badge\&logo=flask)
![AI](https://img.shields.io/badge/AI-Azure_OpenAI-purple?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Entra_ID-green?style=for-the-badge)

---

## Project Overview

The **Enterprise Azure Native AI Processing Platform** is a sophisticated, cloud-native, microservices-based solution designed for enterprise organizations to intelligently process, analyze, and summarize diverse document types (PDFs, images, audio files) using advanced artificial intelligence capabilities. Built entirely on **Microsoft Azure** cloud infrastructure with **Azure Entra ID** authentication and authorization, this platform leverages cutting-edge AI services to extract, understand, and synthesize information from unstructured data at scale.

### Project Purpose

Organizations today struggle with information overload—mountains of documents, images, and audio files that contain valuable insights but are too time-consuming to process manually. This platform solves that problem by:

- **Automating multi-format document processing** - Simultaneously handle PDFs, images, and audio files through intelligent format detection
- **Extracting actionable intelligence** - Use Azure Cognitive Services for OCR, speech-to-text transcription, and content extraction
- **Generating executive summaries** - Leverage Azure OpenAI to produce concise, contextually-relevant summaries of processed content
- **Ensuring enterprise-grade security** - Integrate Azure Entra ID for single sign-on, Azure Key Vault for secrets management, and Azure SQL for audit logging
- **Scaling asynchronously** - Process jobs without blocking user interactions through Azure Service Bus queue-based architecture
- **Maintaining audit compliance** - Track all operations, user actions, and data access for regulatory compliance and security investigations

### Key Use Cases

- **Document Processing Pipelines**: Automate bulk processing of contracts, invoices, reports, and applications
- **Knowledge Management**: Extract and catalog insights from company archives, training materials, and institutional documents
- **Compliance & Audit**: Maintain detailed audit trails of all processed documents and user actions for regulatory requirements
- **Content Intelligence**: Generate automated summaries for executive dashboards and reporting systems
- **Multi-media Analysis**: Process diverse content types (written, visual, audio) in a single unified platform

---

# 📌 Project Overview

The **Enterprise Azure Native AI Processing Platform** is a sophisticated, cloud-native, microservices-based solution engineered for enterprise organizations to intelligently process, analyze, summarize, and manage diverse document types including:

* 📄 PDFs
* 🖼️ Images
* 🎙️ Audio Files

Built entirely on the **Microsoft Azure ecosystem**, the platform integrates:

* 🔐 Azure Entra ID
* 🧠 Azure OpenAI
* 👁️ Azure Cognitive Services
* ☁️ Azure Blob Storage
* 📨 Azure Service Bus
* 🗄️ Azure SQL Database

to deliver secure, scalable, AI-driven document intelligence at enterprise scale.

---

# 🎯 Project Purpose

Modern enterprises struggle with massive volumes of unstructured information.
This platform automates the extraction of insights from documents, images, and audio files using advanced AI services.

## ✨ Core Objectives

### 📂 Intelligent Multi-format Processing

Automatically detect and process:

* PDFs
* Images
* Audio content

### 🧠 AI-Powered Intelligence Extraction

Leverage Azure AI services for:

* OCR
* Speech-to-text
* Text extraction
* Semantic analysis

### 📝 Executive-Level Summarization

Generate concise AI-powered summaries using Azure OpenAI.

### 🔐 Enterprise Security

Built with:

* Azure Entra ID (SSO & RBAC)
* Azure Key Vault
* Azure SQL Audit Logging

### ⚡ Asynchronous Scalability

Queue-driven architecture using Azure Service Bus for non-blocking processing.

### 📋 Compliance & Auditability

Track:

* User actions
* Document access
* Processing events
* Administrative activities

---

# 💼 Key Enterprise Use Cases

| Use Case                   | Description                                                |
| -------------------------- | ---------------------------------------------------------- |
| 📑 Document Processing     | Automate processing of invoices, contracts, forms, reports |
| 🧠 Knowledge Management    | Extract organizational insights from archives              |
| 🛡️ Compliance & Audit     | Maintain immutable audit trails                            |
| 📊 Executive Reporting     | Generate AI-powered summaries                              |
| 🎧 Multimedia Intelligence | Unified processing for documents, images, and audio        |

---

## Technology Stack

### Cloud Platform & Identity
- **Azure Cloud**: Entire platform runs on Microsoft Azure cloud infrastructure
- **Azure Entra ID**: Enterprise identity provider for SSO, user management, and role-based access control
- **Azure Key Vault**: Centralized secrets management (API keys, connection strings, certificates)
- **Azure SQL Database**: Relational database for persistent job tracking and audit logs

### AI & Cognitive Services
- **Azure Cognitive Services - Vision**: OCR (Optical Character Recognition) for extracting text from images and PDFs
- **Azure Cognitive Services - Speech**: Speech-to-text transcription for audio file processing
- **Azure OpenAI (Foundry)**: GPT-based models for intelligent text summarization and content analysis
- **Azure Applied AI**: Advanced document understanding and entity extraction

### Data & Storage
- **Azure Blob Storage**: Scalable object storage for uploaded documents and processed files
- **Azure Service Bus**: Message queue for asynchronous job processing and worker coordination
- **Azure SQL Database**: Transactional database with retry logic and job status tracking

### Application Architecture
- **Python Flask**: Backend microservices for API and frontend web application
- **Docker & Docker Compose**: Containerized deployment with orchestrated microservices
- **Nginx**: Reverse proxy and load balancer for routing and SSL termination
- **Gunicorn**: WSGI HTTP server for Flask applications

### Development & DevOps
- **Python 3.9+**: Primary development language
- **Git**: Version control system
- **Docker**: Container platform for consistent deployment
- **Azure CLI**: Command-line interface for Azure resource management

---

## Project Structure

```
ENTERPRISE-AI-PLATFORM/
│
├── README.md                          # Project documentation (this file)
├── docker-compose.yml                 # Microservices orchestration
├── .gitignore                         # Git ignore rules
│
├── frontend/                          # Web application (Port 3000)
│   ├── app.py                         # Flask application entry point
│   ├── requirements.txt               # Python dependencies
│   ├── Dockerfile                     # Container configuration
│   ├── templates/                     # HTML templates
│   │   ├── base.html                  # Base template with navigation
│   │   ├── login.html                 # Entra ID login page
│   │   ├── dashboard.html             # Main dashboard with job overview
│   │   ├── upload.html                # File upload interface
│   │   ├── jobs.html                  # Job status tracking
│   │   ├── results.html               # Processed results display
│   │   ├── admin.html                 # Admin panel for system management
│   │   └── audit_logs.html            # Audit log viewer for compliance
│   └── static/                        # CSS, JavaScript, images
│
├── api_service/                       # REST API Backend (Port 5000)
│   ├── app.py                         # API entry point
│   ├── requirements.txt               # Dependencies
│   ├── Dockerfile                     # Container configuration
│   ├── routes/                        # API route definitions
│   │   ├── auth.py                    # Authentication endpoints
│   │   ├── jobs.py                    # Job submission endpoints
│   │   └── results.py                 # Results retrieval endpoints
│   └── middleware/                    # Authentication & validation
│
├── worker_service/                    # Async Job Processing Service
│   ├── requirements.txt               # Python dependencies (Azure SDKs)
│   ├── Dockerfile                     # Container configuration
│   │
│   ├── workers/
│   │   ├── queue_listener.py          # Main entry point - listens to Service Bus
│   │   ├── models.py                  # Job database model
│   │   └── job_processor.py           # Job processing coordination
│   │
│   ├── ai/
│   │   ├── ai_orchestrator.py         # Routes jobs to appropriate AI service
│   │   ├── pdf_extractor.py           # PDF text extraction
│   │   ├── image_processor.py         # Image OCR and analysis
│   │   └── audio_processor.py         # Audio transcription
│   │
│   ├── azure_clients/
│   │   ├── blob_client.py             # Azure Blob Storage integration
│   │   ├── service_bus_client.py      # Azure Service Bus queue operations
│   │   ├── sql_client.py              # Azure SQL Database connection
│   │   ├── keyvault_client.py         # Azure Key Vault secret retrieval
│   │   ├── vision_client.py           # Azure Computer Vision (OCR)
│   │   ├── speech_client.py           # Azure Speech Services
│   │   └── foundry_client.py          # Azure OpenAI Foundry (Summarization)
│   │
│   └── config/
│       ├── settings.py                # Configuration management
│       └── logging.py                 # Logging setup
│
├── nginx/                             # Reverse Proxy (Port 8080)
│   ├── Dockerfile                     # Container configuration
│   └── nginx.conf                     # Route configuration
│
├── migrations/                        # Database migrations
│   └── *.sql                          # Schema setup scripts
│
└── temp_processing/                   # Temporary file storage (local)
    └── (Runtime storage for processing)
```

### Component Responsibilities

| Component | Purpose | Technology | Port |
|-----------|---------|-----------|------|
| **Nginx** | Entry point, routing, reverse proxy, SSL termination | Nginx | 8080 |
| **Frontend** | Web UI, user interactions, job submission | Python Flask | 3000 |
| **API Service** | Business logic, job orchestration, authentication | Python Flask | 5000 |
| **Worker Service** | Asynchronous job processing, AI orchestration | Python (headless) | None |
| **Azure Services** | AI, storage, identity, secrets, database | Azure SDKs | Cloud |

---

## API Endpoints

### Frontend Routes (Web Application - Port 3000)

| HTTP Method | Endpoint | Purpose | Authentication | Response |
|-------------|----------|---------|-----------------|----------|
| `GET` | `/` | Redirect to login or dashboard | Entra ID | Redirect to `/login` or `/dashboard` |
| `GET` | `/login` | Entra ID authentication page | Entra ID OAuth | HTML login page |
| `POST` | `/login/callback` | Handle Entra ID token callback | Entra ID | Session established, redirect to `/dashboard` |
| `GET` | `/logout` | Logout and clear session | Entra ID | Redirect to login page |
| `GET` | `/dashboard` | Main dashboard with job summary | Entra ID | HTML dashboard with job statistics |
| `GET` | `/upload` | File upload page | Entra ID | HTML upload form |
| `POST` | `/upload` | Submit file for processing | Entra ID JWT | JSON: `{job_id, status}` |
| `GET` | `/jobs` | List all user's jobs | Entra ID JWT | HTML jobs page or JSON job list |
| `GET` | `/jobs/<job_id>` | Job status and details | Entra ID JWT | JSON: `{job_id, status, progress, created_at}` |
| `GET` | `/results` | All results page | Entra ID JWT | HTML results page with table |
| `GET` | `/results/<job_id>` | Specific job results | Entra ID JWT | JSON: `{job_id, summary, extracted_text, status}` |
| `GET` | `/admin` | Admin panel | Entra ID + Admin Role | HTML admin dashboard |
| `POST` | `/admin/clear-queue` | Clear Service Bus queue | Entra ID + Admin Role | JSON: `{message: "Queue cleared"}` |
| `GET` | `/audit-logs` | Audit log viewer | Entra ID + Admin/Auditor Role | HTML audit log table |
| `GET` | `/audit-logs/export` | Export audit logs (CSV/JSON) | Entra ID + Admin/Auditor Role | CSV or JSON file download |

### API Service Routes (REST API - Port 5000)

| HTTP Method | Endpoint | Purpose | Authentication | Request Body | Response |
|-------------|----------|---------|-----------------|--------------|----------|
| `POST` | `/api/auth/token` | Obtain JWT token | Entra ID Bearer Token | `{entra_id_token}` | JSON: `{access_token, token_type, expires_in}` |
| `POST` | `/api/jobs/submit` | Submit document for processing | JWT Bearer Token | `{file_id, file_type, priority}` | JSON: `{job_id, status, queue_position}` |
| `GET` | `/api/jobs/<job_id>` | Get job status | JWT Bearer Token | None | JSON: `{job_id, status, progress, error_message}` |
| `GET` | `/api/jobs/user/<user_id>` | List user's jobs | JWT Bearer Token | None | JSON Array: `[{job_id, status, created_at}...]` |
| `DELETE` | `/api/jobs/<job_id>` | Cancel job | JWT Bearer Token | None | JSON: `{message: "Job cancelled"}` |
| `GET` | `/api/results/<job_id>` | Get job results | JWT Bearer Token | None | JSON: `{job_id, summary, extracted_text, metadata}` |
| `POST` | `/api/results/<job_id>/download` | Download results file | JWT Bearer Token | None | Binary file (PDF/JSON/TXT) |
| `POST` | `/api/auth/refresh` | Refresh JWT token | JWT Bearer Token (expired) | None | JSON: `{access_token, expires_in}` |
| `GET` | `/api/health` | Service health check | None (public) | None | JSON: `{status: "healthy", version}` |
| `POST` | `/api/admin/users` | Create/manage users (Admin) | JWT + Admin Role | `{username, email, role}` | JSON: User object |
| `GET` | `/api/admin/stats` | System statistics | JWT + Admin Role | None | JSON: `{total_jobs, processed_today, avg_processing_time}` |

### Worker Service (Internal - No Direct HTTP Access)

The Worker Service operates asynchronously and does not expose HTTP endpoints directly. Communication occurs through:

| Communication Method | Source | Destination | Message Type | Purpose |
|-------------------|--------|-------------|--------------|---------|
| **Azure Service Bus Queue** | API Service | Worker Service | JSON Job Message | Job submission for processing |
| **Azure Service Bus Queue** | Worker Service | API Service | JSON Status Update | Job completion/failure notification |
| **Azure SQL** | Worker Service | Database | SQL Transactions | Job status updates, audit logging |
| **Azure Blob Storage** | Worker Service | Storage | File Operations | Upload results, retrieve input files |
| **Azure Key Vault** | Worker Service | Secrets Store | API Calls | Retrieve connection strings and API keys |

---

## Azure Services Architecture

### 1. **Azure Entra ID (Identity Provider)**

**Purpose**: Single Sign-On (SSO) and centralized identity management

**Integration Points**:
- Frontend login redirects users to Entra ID authentication endpoint
- Users authenticate with corporate credentials
- Platform receives JWT tokens with user information and role claims
- Role-based access control (RBAC) enforced for Admin/Auditor functions

**Security Benefits**:
- No password storage in application (delegated to Azure Entra ID)
- Multi-factor authentication (MFA) support
- Conditional access policies
- Real-time identity verification

### 2. **Azure Blob Storage**

**Purpose**: Scalable, secure file storage for uploads and processed documents

**Data Flow**:
```
User Upload → Frontend → API Service → Blob Storage
Blob Storage → Worker Service → Process → Blob Storage (Results)
Blob Storage → Frontend/API → User Download
```

**Security Implementation**:
- Connection strings stored in Azure Key Vault (not in code/env files)
- SAS tokens for time-limited access
- Encryption at rest (Azure-managed keys or CMK)
- Network isolation via private endpoints (optional)

**File Organization**:
- `/uploads/{user_id}/{timestamp}/{filename}` - Input files
- `/results/{job_id}/{result_type}.json` - Processed results
- `/temp/{job_id}/` - Temporary processing files (auto-cleanup)

### 3. **Azure Service Bus**

**Purpose**: Asynchronous job queue and inter-service messaging

**Architecture**:
```
API Service (Producer) → Service Bus Queue → Worker Service (Consumer)
```

**Job Flow**:
1. User submits file via `/upload` endpoint
2. API Service creates Job record and enqueues message to Service Bus
3. Response returned immediately (job_id) to user
4. Worker Service continuously listens to queue
5. Worker processes job and updates status
6. User polls `/jobs/<job_id>` to check status

**Message Format**:
```json
{
  "job_id": "uuid",
  "user_id": "entra-id-oid",
  "file_url": "https://blob.azure.com/uploads/...",
  "file_type": "pdf|image|audio",
  "priority": "normal|high",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Retry Logic**:
- Dead letter queue for permanently failed jobs
- Worker retries 3 times on transient failures
- Exponential backoff between retries
- Failed jobs logged to audit trail

### 4. **Azure SQL Database**

**Purpose**: Persistent data storage with transactional consistency

**Schema Overview**:
```sql
-- Jobs table
Jobs (
  job_id: UUID PRIMARY KEY,
  user_id: NVARCHAR(255),
  file_path: NVARCHAR(512),
  status: NVARCHAR(50), -- PENDING, PROCESSING, SUCCESS, FAILED
  created_at: DATETIME,
  updated_at: DATETIME,
  retry_count: INT,
  error_message: NVARCHAR(1024)
)

-- Audit logs table
AuditLogs (
  log_id: BIGINT PRIMARY KEY IDENTITY,
  user_id: NVARCHAR(255),
  action: NVARCHAR(100),
  resource_type: NVARCHAR(50),
  resource_id: NVARCHAR(255),
  timestamp: DATETIME,
  ip_address: NVARCHAR(50),
  details: NVARCHAR(MAX)
)

-- Results table
Results (
  result_id: UUID PRIMARY KEY,
  job_id: UUID FOREIGN KEY,
  summary: NVARCHAR(MAX),
  extracted_text: NVARCHAR(MAX),
  metadata: NVARCHAR(MAX) -- JSON
)
```

**Transactional Integrity**:
- Job status updates wrapped in transactions
- Audit logging within same transaction for consistency
- Connection pooling for performance
- Retry logic for transient SQL errors

### 5. **Azure Key Vault**

**Purpose**: Centralized secrets management

**Secrets Stored**:
- Azure Blob Storage connection string
- Azure Service Bus connection string
- Azure SQL Database connection string
- Azure OpenAI API key
- Azure Cognitive Services API keys
- SSL certificates for HTTPS

**Access Pattern**:
```
Application → Managed Identity (MSI) → Azure Key Vault
                        ↓
          Authenticate via Azure Entra ID
                        ↓
           Retrieve secrets securely
```

**Benefits**:
- No secrets in `.env`, code, or Docker images
- Audit trail of secret access
- Automatic secret rotation support
- Role-based access to secrets (principle of least privilege)

### 6. **Azure Cognitive Services**

#### **Computer Vision (OCR)**
- **Use Case**: Extract text from image files and PDFs
- **API**: `analyze_image()` with OCR capability
- **Output**: Structured text with location data

#### **Speech Services**
- **Use Case**: Transcribe audio files to text
- **API**: Speech-to-text with language detection
- **Output**: Transcript text with confidence scores

### 7. **Azure OpenAI (Foundry Model)**

**Purpose**: Intelligent text summarization

**Configuration**:
- Model: GPT-4 or GPT-3.5-Turbo (configurable)
- Temperature: 0.3 (low randomness for consistent output)
- Max Tokens: 300 (enterprise-appropriate summary length)
- System Prompt: Customizable for domain-specific summaries

**Usage**:
```python
SUMMARIZATION_PROMPT = """
You are an enterprise document analyst. Summarize the following document 
in clear, concise bullet points suitable for executive review. 
Focus on key decisions, risks, and actionable items.
"""
```

**Deployment Strategy**:
- Multiple model deployments for redundancy
- Fallback to alternative deployment on timeout
- Request throttling to manage quota limits

---

## Security & Privacy Architecture

### Authentication & Authorization

**Entra ID Integration**:
- Users authenticate via Entra ID (SSO)
- JWT tokens issued with user ID, email, and role claims
- Session tokens stored in secure HTTP-only cookies
- Token expiration and refresh logic implemented
- Logout clears both browser and backend sessions

**RBAC (Role-Based Access Control)**:
```
User Roles:
├── End User (default)
│   ├── Upload documents
│   ├── View own results
│   └── View own job history
├── Admin
│   ├── All user permissions
│   ├── System management
│   ├── Queue management
│   └── User administration
└── Auditor
    ├── View audit logs
    ├── Export compliance reports
    └── No modification privileges
```

### Data Protection

**Encryption in Transit**:
- HTTPS/TLS 1.2+ for all communications
- Service-to-service communication via private network
- Azure managed SSL certificates

**Encryption at Rest**:
- Azure Blob Storage: Microsoft-managed or customer-managed keys
- Azure SQL Database: Transparent Data Encryption (TDE)
- Azure Key Vault: HSM-backed encryption
- Temporary files: Encrypted with auto-deletion

**Data Minimization**:
- Upload only what's necessary
- Automatic cleanup of temporary files after processing
- Results retention policy (configurable, default 90 days)
- User data deletion on account termination

### Audit & Compliance

**Comprehensive Audit Logging**:
```
Audited Events:
- User login/logout (timestamp, IP, status)
- Document uploads (user, file size, file type, hash)
- Processing completion (job status, duration)
- Result access (user, job_id, timestamp)
- Administrative actions (user, action, target)
- Errors & retries (job_id, error details, retry count)
```

**Compliance Features**:
- Immutable audit logs (write-once)
- Audit log export (CSV, JSON) for compliance reviews
- Data residency enforcement (Azure region selection)
- Right-to-deletion support (GDPR compliance)
- Data export functionality (user data portability)

### API Security

**Request Validation**:
- Input sanitization (prevent injection attacks)
- File type validation (whitelist: PDF, PNG, JPG, MP3, WAV)
- File size limits (max 100 MB per document)
- Rate limiting (prevent brute force/DoS)

**Error Handling**:
- Generic error messages to users (no stack traces)
- Detailed error logging internally (for debugging)
- Sensitive data scrubbing from logs
- Proper HTTP status codes (400, 401, 403, 500)

### Infrastructure Security

**Network Isolation**:
- Azure Virtual Network (VNet) for service isolation
- Private endpoints for Azure services (optional)
- Network Security Groups (NSGs) for ingress/egress rules
- DDoS protection via Azure DDoS Protection service

**Container Security**:
- Docker images scanned for vulnerabilities
- Minimal base images (Alpine, Distroless where possible)
- No hardcoded secrets in images
- Runtime security monitoring via Azure Defender

---

## Deployment & Setup

### Prerequisites

- Microsoft Azure subscription with resource group
- Azure Entra ID tenant configured with application registration
- Docker and Docker Compose installed locally
- Python 3.9+ (for local development)
- Git for version control

### Environment Configuration

Create a `.env` file (never commit this to Git):

```env
# Azure Entra ID
ENTRA_CLIENT_ID=your-app-registration-id
ENTRA_TENANT_ID=your-tenant-id
ENTRA_REDIRECT_URI=https://yourdomain.com/login/callback

# Azure Key Vault
KEYVAULT_URL=https://your-keyvault.vault.azure.net/

# Azure Service Bus
SERVICE_BUS_NAMESPACE=your-namespace.servicebus.windows.net
SERVICE_BUS_QUEUE_NAME=document-processing-queue

# Azure SQL Database
SQL_SERVER=your-server.database.windows.net
SQL_DATABASE=enterprise_ai_db
SQL_USERNAME=sqladmin

# Azure Blob Storage
BLOB_ACCOUNT_NAME=yourstorageaccount
BLOB_CONTAINER_NAME=enterprise-ai-documents

# Azure Cognitive Services
VISION_ENDPOINT=https://your-region.api.cognitive.microsoft.com/
VISION_API_KEY_VAULT_NAME=vision-api-key

SPEECH_ENDPOINT=https://your-region.tts.speech.microsoft.com/
SPEECH_API_KEY_VAULT_NAME=speech-api-key

# Azure OpenAI
OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
OPENAI_API_VERSION=2024-02-01
OPENAI_DEPLOYMENT_NAME=gpt-4-summary

# Application Configuration
APP_ENV=production
LOG_LEVEL=INFO
MAX_UPLOAD_SIZE_MB=100
RESULT_RETENTION_DAYS=90
SESSION_SECRET_KEY=your-secure-random-key
```

### Local Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/enterprise-ai-platform.git
cd enterprise-ai-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Copy .env.example to .env and configure
cp .env.example .env
# Edit .env with your Azure credentials

# Start services with Docker Compose
docker-compose -f docker-compose.yml up -d

# Check service health
curl http://localhost:8080/api/health

# View logs
docker-compose logs -f
```

### Azure Cloud Deployment

```bash
# 1. Create Azure resources
az group create --name enterprise-ai-rg --location eastus

# 2. Create container registry
az acr create --resource-group enterprise-ai-rg \
  --name youracr --sku Basic

# 3. Deploy to Azure Container Instances or AKS
az container create --resource-group enterprise-ai-rg \
  --file docker-compose.yml

# 4. Configure SSL certificate (via Azure Application Gateway)
# Reference: Azure docs on SSL termination

# 5. Enable monitoring
az monitor metrics list-definitions --resource-type Microsoft.Web/sites
```

---

## Workflow & Job Processing

### End-to-End Job Flow

```
1. USER INTERACTION
   User → Login (Entra ID) → Dashboard → Upload Document

2. API PROCESSING
   Frontend → POST /upload → API Service
   API Service → Create Job Record → Queue Message → Azure Service Bus
   API Service → Return Job ID to Frontend

3. ASYNC PROCESSING (Worker Service)
   Worker Listener → Poll Service Bus → Dequeue Message
   Worker → Fetch File from Blob Storage
   Worker → Detect File Type
   Worker → Route to Appropriate AI Service
   
4. AI PROCESSING (Conditional)
   IF PDF → PDFExtractor → Text Extraction
   IF Image → Computer Vision (OCR) → Text Extraction
   IF Audio → Speech Services → Transcription
   
5. SUMMARIZATION
   Extracted Text → Azure OpenAI Foundry → Summary
   
6. STORAGE & NOTIFICATION
   Worker → Save Results to Blob Storage
   Worker → Update Job Status in SQL Database
   Worker → Audit Log Entry
   
7. USER RESULT RETRIEVAL
   User → Poll /jobs/<job_id> → View Status
   Status COMPLETE → User → /results/<job_id> → View Summary
   User → Optional: Download Full Report
```

### Processing Status States

```
PENDING        → Job created, waiting in queue
↓
PROCESSING     → Actively being processed by worker
↓
SUCCESS        → Job completed, results available
              OR
FAILED         → Job failed after retries, error logged
              OR
CANCELLED      → User or admin cancelled job
```

---

## Monitoring & Maintenance

### Health Checks

```bash
# API Service health
curl http://localhost:5000/api/health

# Frontend service health  
curl http://localhost:3000/health

# Worker Service (check via logs)
docker-compose logs worker_service | grep -i "listening\|health"
```

### Logging

All services log to:
- **Console Output**: Real-time visibility via `docker-compose logs`
- **Azure Monitor**: Centralized logging via Application Insights
- **Database**: Audit events stored in SQL for compliance

Log Levels:
- `INFO`: Normal operation, job submissions/completions
- `WARNING`: Transient failures, retries
- `ERROR`: Permanent failures, configuration issues
- `DEBUG`: Detailed processing steps (dev only)

### Performance Optimization

- **Queue Throughput**: Adjust worker concurrency in `docker-compose.yml`
- **Database**: Enable connection pooling, indexing on frequently queried columns
- **Blob Storage**: Implement tiered storage for archived results
- **OpenAI API**: Use model caching, request batching

---

## Contributing & Development

### Code Standards

- **Python**: PEP 8 compliance, type hints
- **Documentation**: Docstrings for all public functions/classes
- **Testing**: Minimum 80% code coverage
- **Security**: No hardcoded secrets, input validation required

### Development Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes and test locally
docker-compose up -d
pytest tests/

# Commit with conventional commits
git commit -m "feat: add new feature"

# Push and create pull request
git push origin feature/new-feature
```

### Testing

```bash
# Run unit tests
pytest tests/unit/

# Run integration tests (requires Docker)
pytest tests/integration/

# Run with coverage
pytest --cov=app tests/
```

---

## Troubleshooting

### Worker Service Not Processing Jobs

```bash
# Check Service Bus connection
docker-compose exec worker_service python -c "from azure_clients.service_bus_client import ServiceBusClient; ServiceBusClient().check_connection()"

# Check queue messages
az servicebus queue peek --resource-group enterprise-ai-rg \
  --namespace-name your-namespace \
  --name document-processing-queue
```

### Blob Storage Upload Failures

```bash
# Verify storage account connectivity
docker-compose exec api_service python -c "from azure_clients.blob_client import BlobClient; BlobClient().list_containers()"

# Check Key Vault access
docker-compose exec api_service python -c "from azure_clients.keyvault_client import KeyVaultClient; KeyVaultClient().get_secret('blob-connection-string')"
```

### Job Stuck in PROCESSING State

```bash
# Check worker logs
docker-compose logs worker_service | tail -100

# Manually requeue job
docker-compose exec api_service python -c "from workers.models import Job; Job.objects.filter(job_id='xxx').update(status='PENDING')"
```

---

## Security Considerations & Best Practices

### DO's ✅

- ✅ Store all secrets in Azure Key Vault
- ✅ Use Managed Identity for Azure service authentication
- ✅ Enable MFA for all user accounts in Entra ID
- ✅ Review audit logs regularly for suspicious activity
- ✅ Keep Azure SDKs and dependencies updated
- ✅ Use HTTPS for all external communications
- ✅ Implement rate limiting on public APIs
- ✅ Encrypt sensitive data in transit and at rest
- ✅ Follow principle of least privilege for IAM roles

### DON'Ts ❌

- ❌ Never commit `.env` files or secrets to Git
- ❌ Never use shared credentials across environments
- ❌ Never disable authentication for testing (even temporarily)
- ❌ Never log user PII or sensitive document content
- ❌ Never use development credentials in production
- ❌ Never expose detailed error messages to users
- ❌ Never process unvalidated file uploads directly
- ❌ Never store files indefinitely without retention policy

---

## License

This project is proprietary and confidential. All rights reserved.

For inquiries, contact: [Your Organization Security Team]

---

## Support & Contact

**Documentation**: See `/docs` folder for detailed architecture and API specifications

**Issues & Bug Reports**: Submit via internal issue tracking system

**Security Concerns**: Report to: security@yourorganization.com

**Azure Support**: Azure Support Portal (your subscription)

---

**Last Updated**: January 2024

**Version**: 1.0.0

**Status**: Production Ready ✅
