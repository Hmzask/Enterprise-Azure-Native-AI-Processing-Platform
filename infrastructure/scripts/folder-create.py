import os

# =========================================
# ENTERPRISE AI PLATFORM STRUCTURE CREATOR
# =========================================

folders = [
    # Frontend
    "frontend/templates",
    "frontend/static/css",
    "frontend/static/js",
    "frontend/static/uploads",

    # API Service
    "api_service/app/routes",
    "api_service/app/controllers",
    "api_service/app/services",
    "api_service/app/middleware",
    "api_service/app/auth",
    "api_service/app/azure",
    "api_service/app/models",
    "api_service/app/schemas",
    "api_service/app/utils",
    "api_service/app/config",
    "api_service/tests",
    "api_service/migrations",

    # Worker Service
    "worker_service/workers",
    "worker_service/ai",
    "worker_service/azure",
    "worker_service/tests",

    # Azure Functions
    "function-app/BlobTrigger",
    "function-app/QueueTrigger",

    # Infrastructure
    "infrastructure/terraform",
    "infrastructure/bicep",
    "infrastructure/scripts",

    # Documentation
    "docs/diagrams",

    # Monitoring
    "monitoring/dashboards",
    "monitoring/alerts",
    "monitoring/appinsights",

    # Nginx
    "nginx",

    # GitHub Actions
    ".github/workflows",

    # Scripts
    "scripts",
]

# =========================================
# FILES TO CREATE
# =========================================

files = {
    # Root files
    "README.md": "# Enterprise AI Platform\n",
    ".env": "",
    ".gitignore": """
__pycache__/
*.pyc
.env
venv/
node_modules/
*.db
.azure/
.idea/
.vscode/
""",
    "docker-compose.yml": "",
    "requirements.txt": "",
    "Makefile": "",

    # Frontend
    "frontend/app.py": "",
    "frontend/templates/index.html": "",
    "frontend/static/css/style.css": "",
    "frontend/static/js/app.js": "",

    # API Service
    "api-service/run.py": "",
    "api-service/Dockerfile": "",
    "api-service/requirements.txt": "",
    "api-service/app/__init__.py": "",
    "api-service/app/routes/__init__.py": "",
    "api-service/app/controllers/__init__.py": "",
    "api-service/app/services/__init__.py": "",
    "api-service/app/middleware/__init__.py": "",
    "api-service/app/auth/__init__.py": "",
    "api-service/app/azure/__init__.py": "",
    "api-service/app/models/__init__.py": "",
    "api-service/app/schemas/__init__.py": "",
    "api-service/app/utils/__init__.py": "",
    "api-service/app/config/__init__.py": "",

    # Worker Service
    "worker-service/Dockerfile": "",
    "worker-service/requirements.txt": "",
    "worker-service/workers/ai_worker.py": "",
    "worker-service/workers/queue_listener.py": "",
    "worker-service/workers/blob_processor.py": "",
    "worker-service/workers/retry_handler.py": "",

    "worker-service/ai/summarizer.py": "",
    "worker-service/ai/pii_detector.py": "",
    "worker-service/ai/speech_to_text.py": "",
    "worker-service/ai/image_ocr.py": "",
    "worker-service/ai/embeddings.py": "",
    "worker-service/ai/moderation.py": "",

    "worker-service/azure/blob_client.py": "",
    "worker-service/azure/servicebus_client.py": "",
    "worker-service/azure/foundry_client.py": "",
    "worker-service/azure/keyvault_client.py": "",
    "worker-service/azure/sql_client.py": "",

    # Function App
    "function-app/host.json": "{}",
    "function-app/local.settings.json": "{}",
    "function-app/requirements.txt": "",

    # Terraform
    "infrastructure/terraform/main.tf": "",
    "infrastructure/terraform/variables.tf": "",
    "infrastructure/terraform/outputs.tf": "",
    "infrastructure/terraform/providers.tf": "",

    # Bicep
    "infrastructure/bicep/storage.bicep": "",
    "infrastructure/bicep/sql.bicep": "",
    "infrastructure/bicep/servicebus.bicep": "",
    "infrastructure/bicep/keyvault.bicep": "",

    # Infra Scripts
    "infrastructure/scripts/deploy.sh": "",
    "infrastructure/scripts/setup.ps1": "",

    # Docs
    "docs/architecture.md": "# Architecture\n",
    "docs/api-docs.md": "# API Docs\n",
    "docs/security.md": "# Security\n",
    "docs/deployment.md": "# Deployment\n",

    # Monitoring
    "monitoring/appinsights/config.json": "{}",

    # Nginx
    "nginx/nginx.conf": "",
    "nginx/Dockerfile": "",

    # GitHub Actions
    ".github/workflows/ci.yml": "",
    ".github/workflows/cd.yml": "",
    ".github/workflows/security-scan.yml": "",

    # Scripts
    "scripts/bootstrap.sh": "",
    "scripts/seed_data.py": "",
}

# =========================================
# CREATE FOLDERS
# =========================================

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# =========================================
# CREATE FILES
# =========================================

for file_path, content in files.items():

    parent_dir = os.path.dirname(file_path)

    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("✅ Enterprise AI Platform structure created successfully!")
