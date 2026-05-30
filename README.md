# Enterprise Azure-Native AI Processing Platform

<div align="center">

![Enterprise AI Platform](https://img.shields.io/badge/Enterprise-AI%20Platform-blue?style=flat-square&logo=microsoft-azure)
![Python](https://img.shields.io/badge/Python-3.9+-green?style=flat-square&logo=python)
![React](https://img.shields.io/badge/React-18+-blue?style=flat-square&logo=react)
![Docker](https://img.shields.io/badge/Docker-Compose-blue?style=flat-square&logo=docker)
![Azure](https://img.shields.io/badge/Cloud-Microsoft%20Azure-0078D4?style=flat-square&logo=microsoft-azure)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A production-grade, cloud-native AI processing platform built on Microsoft Azure, designed to intelligently process and analyze diverse media types including PDFs, images, and audio files using advanced machine learning and cognitive services.

[Features](#-features) • [Architecture](#-system-architecture) • [Getting Started](#-getting-started) • [API Documentation](#-api-endpoints) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Technical Stack](#-technical-stack)
- [Prerequisites](#-prerequisites)
- [Getting Started](#-getting-started)
- [API Endpoints](#-api-endpoints)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Development](#-development)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

The **Enterprise Azure-Native AI Processing Platform** is a sophisticated, containerized solution designed for enterprises that need to process, analyze, and extract insights from unstructured data at scale. By leveraging Microsoft Azure's cognitive services and OpenAI's GPT models, the platform provides:

- **Automated Document Processing**: Extract text and data from PDFs, images, and audio files
- **Intelligent Summarization**: Generate concise summaries of extracted content using advanced NLP
- **Scalable Architecture**: Asynchronous job processing with robust error handling and retry mechanisms
- **Enterprise Security**: Integration with Azure Key Vault for credential management
- **Cloud-Native Design**: Built for Azure with complete containerization and orchestration support

### Key Benefits

✅ **Fully Automated** - End-to-end processing pipeline with minimal manual intervention  
✅ **Highly Available** - Distributed microservices architecture with health monitoring  
✅ **Enterprise-Ready** - Security-first approach with Azure Key Vault integration  
✅ **Scalable** - Handle multiple processing requests concurrently with queue-based architecture  
✅ **Intelligent** - AI-powered text extraction and summarization powered by Azure AI and OpenAI  

---

## ⚡ Features

### Core Capabilities

| Feature | Description | Technology |
|---------|-------------|-----------|
| **PDF Processing** | Extract text and data from PDF documents with high accuracy | PyMuPDF (fitz) |
| **Image OCR** | Optical Character Recognition for images and scanned documents | Azure Computer Vision API |
| **Audio Transcription** | Convert audio files to text with automatic format conversion | Azure Speech Services |
| **Text Summarization** | Generate intelligent summaries of extracted content | OpenAI GPT Models |
| **Async Job Processing** | Handle multiple jobs concurrently with queue-based architecture | Azure Service Bus |
| **Error Handling** | Robust retry logic with exponential backoff and dead-letter queue handling | Azure Service Bus |
| **Secure Storage** | Store documents and results in cloud storage with encryption | Azure Blob Storage |
| **Credential Management** | Centralized secret and credential management | Azure Key Vault |

### Enterprise Features

- 🔐 **Zero-Trust Security**: Credential-less authentication using Managed Identity
- 📊 **Job Tracking**: Real-time job status monitoring and result retrieval
- 🔄 **Automatic Retries**: Intelligent retry mechanism for failed operations
- 📈 **Scalability**: Horizontal scaling through containerized microservices
- 🌐 **Multi-Region Support**: Ready for deployment across Azure regions
- 📝 **Comprehensive Logging**: Structured logging for audit and debugging
- ⚡ **High Performance**: Optimized for low-latency processing

---

## 🏗️ System Architecture

### Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────────┐
│                         ENTERPRISE NETWORK                           │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                   NGINX REVERSE PROXY (Port 8080)           │   │
│  │              Load Balancing & Request Routing               │   │
│  └──────────────────┬──────────────────┬──────────────────────┘   │
│                     │                  │                           │
│         ┌───────────┴────────┐    ┌────┴──────────────┐          │
│         ▼                    ▼    ▼                   ▼           │
│  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐  │
│  │   FRONTEND       │ │   API SERVICE    │ │  WORKER SERVICE  │  │
│  │   (React)        │ │   (Flask)        │ │  (Job Processor) │  │
│  │  Port: 3000      │ │   Port: 5000     │ │ Async Queue Cons │  │
│  │                  │ │                  │ │                  │  │
│  │ • Job Upload     │ │ • Job Submit API │ │ • File Download  │  │
│  │ • Status Display │ │ • Status Check   │ │ • AI Processing  │  │
│  │ • Result View    │ │ • Result Fetch   │ │ • Data Persist   │  │
│  └──────────────────┘ └────────┬─────────┘ └────────┬─────────┘  │
│                                 │                    │             │
│         ┌───────────────────────┴────────┬───────────┴────────┐   │
│         │                                │                    │   │
└─────────┼────────────────────────────────┼────────────────────┼───┘
          │                                │                    │
    ┌─────▼─────┐                  ┌──────▼──────────┐   ┌──────▼─────────┐
    │  DATABASE │                  │  SERVICE BUS    │   │  BLOB STORAGE  │
    │  (SQL)    │◄─────────────────┤  (Message Queue)│   │  (Files)       │
    │           │                  │                 │   │                │
    └───────────┘                  └─────────────────┘   └────────────────┘
                                          ▲
    ┌────────────────────────────────────┘│┌─────────────────────────┐
    │                                      ││  AZURE COGNITIVE SVCS  │
    │            AZURE SERVICES            ││                        │
    │                                      ││ • Vision API (OCR)     │
    ├──────────────────────────────────────┤│ • Speech Services      │
    │                                      ││ • Key Vault            │
    │ • Container Registry                 │└─────────────────────────┘
    │ • Managed Identity                   │
    │ • Monitor & Alerts                   │  ┌──────────────────────┐
    │ • Service Principal Auth             │  │  OPENAI (GPT API)    │
    │                                      │  │                      │
    │                                      │  │ • Text Summarization │
    │                                      │  │ • Content Generation │
    │                                      │  └──────────────────────┘
    └──────────────────────────────────────┘
```

### Data Flow

```
1. FILE UPLOAD
   User → Frontend → API Service → Azure Blob Storage
                  ↓
              Create Job Record in DB

2. ASYNC PROCESSING
   API Service → Service Bus Queue → Worker Service
                                   ↓
                          Download from Blob Storage
                                   ↓
                          AI Orchestration:
                          • PDF Extraction
                          • Image OCR
                          • Audio Transcription
                                   ↓
                          OpenAI Summarization
                                   ↓
                          Store Results in DB

3. RESULT RETRIEVAL
   Frontend → API Service → Database → Client
```

---

## 🛠️ Technical Stack

### Backend Services

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| API Framework | Flask | 3.1.3 | RESTful API server |
| ORM | SQLAlchemy | 2.0.49 | Database abstraction |
| Task Queue | Azure Service Bus | 7.14.3 | Async job processing |
| Web Server | Werkzeug | 3.1.8 | WSGI server |

### Azure Services

| Service | Package | Version | Use Case |
|---------|---------|---------|----------|
| Blob Storage | azure-storage-blob | 12.29.0 | File storage & retrieval |
| Service Bus | azure-servicebus | 7.14.3 | Message queue & job distribution |
| Cognitive Services | azure-cognitiveservices-speech | 1.50.0 | Audio transcription |
| Vision API | azure-ai-vision-imageanalysis | 1.0.0 | Image OCR & text extraction |
| Key Vault | azure-identity | 1.25.3 | Secret & credential management |

### AI & Processing

| Component | Package | Version | Function |
|-----------|---------|---------|----------|
| LLM | openai | 2.38.0 | Text summarization & generation |
| PDF Processing | PyMuPDF | 1.27.2.3 | PDF text extraction |
| File Conversion | ffmpeg | Latest | Audio format conversion |
| Database | SQL Server | 2019+ | Data persistence |

### Infrastructure

| Tool | Purpose |
|------|---------|
| Docker | Containerization |
| Docker Compose | Local orchestration |
| Nginx | Reverse proxy & load balancing |
| Python | Runtime environment |

---

## 📦 Prerequisites

### System Requirements

- **OS**: Linux, macOS, or Windows (with WSL2)
- **Docker**: Version 20.10+
- **Docker Compose**: Version 1.29+
- **Python**: 3.9+ (for local development)
- **Git**: Latest version

### Cloud Requirements

- **Azure Account** with the following services:
  - Azure SQL Database
  - Azure Blob Storage
  - Azure Service Bus
  - Azure Cognitive Services (Vision, Speech)
  - Azure Key Vault
  - Azure Container Registry (optional, for production)

### API Keys & Credentials

You'll need the following credentials configured in `.env`:

```
# Azure SQL
AZURE_SQL_SERVER=
AZURE_SQL_DATABASE=
AZURE_SQL_USER=
AZURE_SQL_PASSWORD=

# Azure Storage
AZURE_STORAGE_ACCOUNT_NAME=
AZURE_STORAGE_ACCOUNT_KEY=

# Azure Service Bus
AZURE_SERVICE_BUS_CONNECTION_STRING=
AZURE_SERVICE_BUS_QUEUE=

# Azure Cognitive Services
AZURE_VISION_ENDPOINT=
AZURE_VISION_KEY=
AZURE_SPEECH_KEY=
AZURE_SPEECH_REGION=

# OpenAI
OPENAI_API_KEY=
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Hmzask/Enterprise-Azure-Native-AI-Processing-Platform.git
cd Enterprise-Azure-Native-AI-Processing-Platform
```

### 2. Configure Environment Variables

```bash
# Copy the environment template
cp .env.example .env

# Edit with your Azure credentials and API keys
nano .env
```

### 3. Start the Platform

```bash
# Build and start all services
docker-compose up -d --build

# View logs
docker-compose logs -f

# Check service health
docker-compose ps
```

### 4. Verify Deployment

```bash
# API Service Health Check
curl -X GET http://localhost:5000/health

# Frontend Access
open http://localhost:3000

# Nginx Proxy
open http://localhost:8080
```

### 5. Test Processing

```bash
# Upload a file for processing
curl -X POST http://localhost:5000/api/jobs \
  -F "file=@document.pdf" \
  -F "file_type=pdf"

# Check job status
curl -X GET http://localhost:5000/api/jobs/{job_id}

# Retrieve results
curl -X GET http://localhost:5000/api/jobs/{job_id}/results
```

---

## 📡 API Endpoints

### Base URL

```
http://localhost:5000/api
```

### Core Endpoints

#### Job Management

| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| **POST** | `/jobs` | Submit a new file for processing | `file` (multipart), `file_type` (pdf\|image\|audio) | `{ "job_id": "uuid", "status": "PENDING" }` |
| **GET** | `/jobs/{job_id}` | Retrieve job details and current status | - | `{ "job_id": "uuid", "status": "PROCESSING", "created_at": "2024-01-01T00:00:00Z", "completed_at": null }` |
| **GET** | `/jobs/{job_id}/results` | Fetch processing results | - | `{ "extracted_text": "...", "summary": "...", "job_id": "uuid" }` |
| **GET** | `/jobs` | List all jobs with pagination | `?page=1&limit=20` | `{ "jobs": [...], "total": 150, "page": 1 }` |
| **DELETE** | `/jobs/{job_id}` | Cancel and delete a job | - | `{ "status": "DELETED", "job_id": "uuid" }` |

#### Health & Status

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| **GET** | `/health` | Service health check | `{ "status": "healthy", "timestamp": "2024-01-01T00:00:00Z" }` |
| **GET** | `/status/workers` | Check worker service status | `{ "workers_active": 3, "jobs_processing": 5 }` |
| **GET** | `/status/queue` | Check message queue status | `{ "messages_pending": 12, "dead_letters": 0 }` |

### Request/Response Examples

#### Submit a PDF for Processing

```bash
curl -X POST http://localhost:5000/api/jobs \
  -H "Content-Type: multipart/form-data" \
  -F "file=@financial_report.pdf" \
  -F "file_type=pdf"
```

**Response (201 Created):**
```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "PENDING",
  "file_name": "financial_report.pdf",
  "file_type": "pdf",
  "created_at": "2024-01-15T10:30:45Z",
  "estimated_wait_time": "30s"
}
```

#### Check Job Status

```bash
curl -X GET http://localhost:5000/api/jobs/550e8400-e29b-41d4-a716-446655440000
```

**Response (200 OK):**
```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "COMPLETED",
  "file_name": "financial_report.pdf",
  "file_type": "pdf",
  "created_at": "2024-01-15T10:30:45Z",
  "completed_at": "2024-01-15T10:32:15Z",
  "processing_time_seconds": 90
}
```

#### Retrieve Processing Results

```bash
curl -X GET http://localhost:5000/api/jobs/550e8400-e29b-41d4-a716-446655440000/results
```

**Response (200 OK):**
```json
{
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "COMPLETED",
  "ai_result": {
    "extracted_text": "The financial performance of Q4 2023 shows...",
    "summary": "Company achieved 15% revenue growth in Q4 2023, driven by increased market demand..."
  },
  "processing_metadata": {
    "text_length": 5432,
    "processing_duration_ms": 2145,
    "worker_instance": "enterprise_worker_001"
  }
}
```

### Error Responses

#### 400 Bad Request
```json
{
  "error": "INVALID_REQUEST",
  "message": "file_type must be one of: pdf, image, audio",
  "timestamp": "2024-01-15T10:30:45Z"
}
```

#### 404 Not Found
```json
{
  "error": "JOB_NOT_FOUND",
  "message": "Job with ID 550e8400-e29b-41d4-a716-446655440000 not found",
  "timestamp": "2024-01-15T10:30:45Z"
}
```

#### 500 Internal Server Error
```json
{
  "error": "PROCESSING_FAILED",
  "message": "An error occurred while processing the file",
  "job_id": "550e8400-e29b-41d4-a716-446655440000",
  "timestamp": "2024-01-15T10:30:45Z"
}
```

---

## 📂 Project Structure

```
Enterprise-Azure-Native-AI-Processing-Platform/
├── README.md                          # Project documentation
├── docker-compose.yml                 # Multi-container orchestration
├── .env.example                       # Environment variables template
├── .gitignore                         # Git ignore rules
│
├── api_service/                       # Flask API Server
│   ├── Dockerfile                     # Container image definition
│   ├── requirements.txt               # Python dependencies
│   ├── main.py                        # Application entry point
│   └── ...
│
├── worker_service/                    # Async Job Processor
│   ├── Dockerfile                     # Container image definition
│   ├── requirements.txt               # Python dependencies
│   ├── main.py                        # Worker entry point
│   ├── ai/                            # AI Processing modules
│   │   ├── ai_orchestrator.py        # Main processing orchestrator
│   │   ├── pdf_extractor.py          # PDF text extraction
│   │   ├── image_ocr.py              # Image OCR service
│   │   ├── speech_to_text.py         # Audio transcription
│   │   └── summarizer.py             # Text summarization
│   ├── azure_clients/                # Azure Service Clients
│   │   ├── blob_client.py            # Blob Storage operations
│   │   ├── sql_client.py             # SQL Database operations
│   │   ├── keyvault_client.py        # Key Vault integration
│   │   └── foundry_client.py         # OpenAI integration
│   ├── workers/                      # Worker logic
│   │   ├── queue_listener.py         # Service Bus queue listener
│   │   ├── worker_db.py              # Database configuration
│   │   └── models.py                 # Data models
│   └── logger.py                      # Structured logging
│
├── frontend/                          # React Web Application
│   ├── Dockerfile                     # Container image definition
│   ├── package.json                   # Node dependencies
│   ├── src/                           # React components & logic
│   └── public/                        # Static assets
│
├── nginx/                             # Reverse Proxy Configuration
│   ├── Dockerfile                     # Container image definition
│   ├── nginx.conf                     # Nginx configuration
│   └── ...
│
├── migrations/                        # Database Migrations
│   ├── versions/                      # Migration scripts
│   ├── env.py                         # Alembic configuration
│   └── ...
│
└── temp_processing/                   # Temporary file storage
    └── .gitkeep
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# ====== API SERVICE ======
FLASK_ENV=production
FLASK_APP=main.py
API_PORT=5000
API_HOST=0.0.0.0

# ====== DATABASE ======
AZURE_SQL_SERVER=your-server.database.windows.net
AZURE_SQL_DATABASE=your-database
AZURE_SQL_USER=your-username
AZURE_SQL_PASSWORD=your-password
DATABASE_URL=mssql+pyodbc://user:password@server/database?driver=ODBC+Driver+17+for+SQL+Server

# ====== AZURE STORAGE ======
AZURE_STORAGE_ACCOUNT_NAME=yourstorageaccount
AZURE_STORAGE_ACCOUNT_KEY=your-account-key
AZURE_STORAGE_CONTAINER=processing-files

# ====== AZURE SERVICE BUS ======
AZURE_SERVICE_BUS_CONNECTION_STRING=Endpoint=sb://...
AZURE_SERVICE_BUS_QUEUE=ai-processing-queue

# ====== AZURE COGNITIVE SERVICES ======
AZURE_VISION_ENDPOINT=https://your-region.api.cognitive.microsoft.com/
AZURE_VISION_KEY=your-vision-key
AZURE_SPEECH_KEY=your-speech-key
AZURE_SPEECH_REGION=your-region

# ====== OPENAI ======
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4

# ====== LOGGING ======
LOG_LEVEL=INFO
LOG_FORMAT=json

# ====== WORKER SERVICE ======
WORKER_TIMEOUT=300
MAX_RETRIES=3
RETRY_BACKOFF_MULTIPLIER=2
```

### Docker Compose Customization

Edit `docker-compose.yml` to adjust:

- Port mappings
- Environment variables per service
- Volume mounts
- Network configuration
- Resource limits

---

## 👨‍💻 Development

### Local Setup (Without Docker)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install API service dependencies
cd api_service
pip install -r requirements.txt
cd ..

# Install worker service dependencies
cd worker_service
pip install -r requirements.txt
cd ..

# Run API service
python api_service/main.py

# Run worker service (in another terminal)
python worker_service/main.py
```

### Running Tests

```bash
# Run unit tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Integration tests
pytest tests/integration/ -v -m integration
```

### Code Quality

```bash
# Format code
black api_service/ worker_service/

# Lint code
flake8 api_service/ worker_service/

# Type checking
mypy api_service/ worker_service/
```

### Database Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "Add new column"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

---

## 🤝 Contributing

We welcome contributions from the community! Here's how to get started:

### Development Workflow

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/Enterprise-Azure-Native-AI-Processing-Platform.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add unit tests for new functionality
   - Update documentation as needed

4. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Create a Pull Request**
   - Provide clear description of changes
   - Link related issues
   - Ensure all tests pass

### Contribution Guidelines

- **Code Style**: Follow PEP 8
- **Testing**: Maintain >80% code coverage
- **Documentation**: Update README and inline comments
- **Commits**: Use clear, descriptive commit messages
- **Issues**: Check existing issues before creating new ones

### Reporting Issues

- Use GitHub Issues for bug reports
- Include steps to reproduce
- Provide error logs and screenshots
- Specify your environment details

---

## 📋 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

MIT © 2024 Enterprise AI Platform Contributors

---

## 📞 Support & Community

### Get Help

- 📖 **Documentation**: See our [wiki](https://github.com/Hmzask/Enterprise-Azure-Native-AI-Processing-Platform/wiki)
- 💬 **Discussions**: Join our [community discussions](https://github.com/Hmzask/Enterprise-Azure-Native-AI-Processing-Platform/discussions)
- 🐛 **Issue Tracker**: Report bugs on [GitHub Issues](https://github.com/Hmzask/Enterprise-Azure-Native-AI-Processing-Platform/issues)
- 📧 **Email**: enterprise-ai@example.com

### Related Resources

- [Azure Services Documentation](https://docs.microsoft.com/azure/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/)
- [Docker Documentation](https://docs.docker.com/)

---

## 🔐 Security

### Reporting Security Vulnerabilities

**Do not** open public issues for security vulnerabilities. Instead, please email `security@example.com` with:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### Security Best Practices

- ✅ Never commit secrets or API keys to the repository
- ✅ Use Azure Key Vault for credential management
- ✅ Rotate API keys regularly
- ✅ Enable Azure Defender for additional protection
- ✅ Use managed identities for Azure service authentication

---

## 🎯 Roadmap

### Version 2.0 (Q2 2024)
- [ ] Multi-language support for OCR
- [ ] Advanced document layout analysis
- [ ] Real-time processing dashboard
- [ ] Batch processing API improvements

### Version 3.0 (Q4 2024)
- [ ] Custom model fine-tuning
- [ ] Advanced document classification
- [ ] Multi-tenant support
- [ ] GraphQL API support

### Future Considerations
- Support for additional file formats (DOCX, XLSX, PPTX)
- On-premises deployment options
- Advanced workflow automation
- Mobile applications

---

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/Hmzask/Enterprise-Azure-Native-AI-Processing-Platform?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/Hmzask/Enterprise-Azure-Native-AI-Processing-Platform?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/Hmzask/Enterprise-Azure-Native-AI-Processing-Platform?style=flat-square)

---

<div align="center">

**[⬆ back to top](#enterprise-azure-native-ai-processing-platform)**

Built with ❤️ for the Enterprise AI Community

</div>
