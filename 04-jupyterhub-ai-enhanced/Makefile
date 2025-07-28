# JupyterHub AI Platform Makefile
# 
# This Makefile provides convenient commands to build, deploy, and manage
# the JupyterHub AI platform with integrated AI tools and services.

.PHONY: help build start stop restart logs clean setup-secrets setup-env \
        build-hub build-singleuser push-images pull-images \
        backup restore status health-check dev-start ollama-start \
        ollama-stop clean-volumes clean-images

# Default target
help: ## Show this help message
	@echo "JupyterHub AI Platform - Available Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "Environment files needed:"
	@echo "  - ai.env (API keys and configuration)"
	@echo "  - secrets/oauth_client_id.txt"
	@echo "  - secrets/oauth_client_secret.txt"

# Variables
COMPOSE_FILE := docker-compose.yml
HUB_IMAGE_NAME := jupyterhub-ai
SINGLEUSER_IMAGE_NAME := jupyter-singleuser-ai
DOCKER_REGISTRY ?= localhost
TAG ?= latest

# Setup and Configuration
setup: setup-dirs setup-secrets setup-env ## Initialize the project (create directories and template files)

setup-dirs: ## Create necessary directories
	@echo "Creating required directories..."
	@mkdir -p secrets examples data
	@mkdir -p backup
	@echo "Directories created successfully!"

setup-secrets: ## Create template secret files (you need to fill them with actual values)
	@echo "Creating secret template files..."
	@mkdir -p secrets
	@if [ ! -f secrets/oauth_client_id.txt ]; then \
		echo "your_github_oauth_client_id" > secrets/oauth_client_id.txt; \
		echo "⚠️  Please edit secrets/oauth_client_id.txt with your GitHub OAuth Client ID"; \
	fi
	@if [ ! -f secrets/oauth_client_secret.txt ]; then \
		echo "your_github_oauth_client_secret" > secrets/oauth_client_secret.txt; \
		echo "⚠️  Please edit secrets/oauth_client_secret.txt with your GitHub OAuth Client Secret"; \
	fi

setup-env: ## Create template environment file
	@if [ ! -f ai.env ]; then \
		echo "Creating ai.env template..."; \
		echo "# JupyterHub Configuration" > ai.env; \
		echo "DOCKER_JUPYTER_IMAGE=jupyter-singleuser-ai:latest" >> ai.env; \
		echo "DOCKER_NOTEBOOK_DIR=/home/jovyan/work" >> ai.env; \
		echo "DOCKER_NETWORK_NAME=jupyterhub-network" >> ai.env; \
		echo "" >> ai.env; \
		echo "# AI API Keys (fill with your actual keys)" >> ai.env; \
		echo "OPENAI_API_KEY=" >> ai.env; \
		echo "OPENAI_API_BASE=https://api.openai.com/v1" >> ai.env; \
		echo "ANTHROPIC_API_KEY=" >> ai.env; \
		echo "ALIYUN_API_KEY=" >> ai.env; \
		echo "ALIYUN_API_BASE=https://dashscope.aliyuncs.com/api/v1" >> ai.env; \
		echo "DEEPSEEK_API_KEY=" >> ai.env; \
		echo "DEEPSEEK_API_BASE=https://api.deepseek.com/v1" >> ai.env; \
		echo "" >> ai.env; \
		echo "# Ollama Configuration" >> ai.env; \
		echo "OLLAMA_URL=http://ollama:11434" >> ai.env; \
		echo "⚠️  Please edit ai.env with your actual API keys"; \
	else \
		echo "ai.env already exists, skipping..."; \
	fi

# Build Commands
build: build-hub build-singleuser ## Build all Docker images

build-hub: ## Build JupyterHub image
	@echo "Building JupyterHub image..."
	docker build -f Dockerfile.jupyterhub -t $(HUB_IMAGE_NAME):$(TAG) .

build-singleuser: ## Build single-user Jupyter image
	@echo "Building single-user Jupyter image..."
	docker build -f Dockerfile.singleuser -t $(SINGLEUSER_IMAGE_NAME):$(TAG) .

# Service Management
start: ## Start all services (default profile)
	@echo "Starting JupyterHub AI platform..."
	docker-compose --profile default up -d
	@echo "✅ JupyterHub is starting up..."
	@echo "📝 Access at: http://localhost:8000"
	@echo "⏳ Please wait a moment for services to initialize"

start-with-ollama: ## Start all services including Ollama
	@echo "Starting JupyterHub AI platform with Ollama..."
	docker-compose --profile default --profile ollama up -d
	@echo "✅ JupyterHub and Ollama are starting up..."
	@echo "📝 JupyterHub: http://localhost:8000"
	@echo "🤖 Ollama API: http://localhost:11434"

stop: ## Stop all services
	@echo "Stopping all services..."
	docker-compose down

restart: ## Restart all services
	@echo "Restarting services..."
	docker-compose restart

# Ollama Management
ollama-start: ## Start only Ollama service
	@echo "Starting Ollama service..."
	docker-compose --profile ollama up -d ollama

ollama-stop: ## Stop Ollama service
	@echo "Stopping Ollama service..."
	docker-compose stop ollama

ollama-pull: ## Pull a model in Ollama (usage: make ollama-pull MODEL=llama2)
	@if [ -z "$(MODEL)" ]; then \
		echo "❌ Please specify MODEL. Example: make ollama-pull MODEL=llama2"; \
		exit 1; \
	fi
	docker-compose exec ollama ollama pull $(MODEL)

ollama-list: ## List available Ollama models
	docker-compose exec ollama ollama list

# Development Commands
dev-start: ## Start in development mode with build
	@echo "Starting in development mode..."
	docker-compose --profile default up --build -d

logs: ## Show logs for all services
	docker-compose logs -f

logs-hub: ## Show logs for JupyterHub only
	docker-compose logs -f hub

logs-ollama: ## Show logs for Ollama only
	docker-compose logs -f ollama

# Status and Health Checks
status: ## Show status of all services
	@echo "Service Status:"
	@docker-compose ps

health-check: ## Check if services are healthy
	@echo "Checking service health..."
	@echo "JupyterHub Hub:"
	@curl -s -o /dev/null -w "HTTP Status: %{http_code}\n" http://localhost:8000/hub/health || echo "❌ JupyterHub not responding"
	@echo "Ollama API:"
	@curl -s -o /dev/null -w "HTTP Status: %{http_code}\n" http://localhost:11434/api/version || echo "❌ Ollama not responding"

# Data Management
backup: ## Backup JupyterHub data and user volumes
	@echo "Creating backup..."
	@mkdir -p backup/$(shell date +%Y%m%d_%H%M%S)
	docker run --rm -v jupyterhub_data:/data -v $(PWD)/backup:/backup alpine \
		tar czf /backup/$(shell date +%Y%m%d_%H%M%S)/jupyterhub_data.tar.gz -C /data .
	@echo "✅ Backup completed in backup/$(shell date +%Y%m%d_%H%M%S)/"

restore: ## Restore from backup (usage: make restore BACKUP_DIR=20240101_120000)
	@if [ -z "$(BACKUP_DIR)" ]; then \
		echo "❌ Please specify BACKUP_DIR. Example: make restore BACKUP_DIR=20240101_120000"; \
		exit 1; \
	fi
	@if [ ! -f "backup/$(BACKUP_DIR)/jupyterhub_data.tar.gz" ]; then \
		echo "❌ Backup file not found: backup/$(BACKUP_DIR)/jupyterhub_data.tar.gz"; \
		exit 1; \
	fi
	@echo "Restoring from backup/$(BACKUP_DIR)..."
	@docker-compose down
	@docker run --rm -v jupyterhub_data:/data -v $(PWD)/backup:/backup alpine \
		tar xzf /backup/$(BACKUP_DIR)/jupyterhub_data.tar.gz -C /data
	@echo "✅ Restore completed"

# Cleanup Commands
clean: ## Stop services and remove containers
	@echo "Cleaning up containers..."
	docker-compose down --remove-orphans

clean-volumes: ## Remove all data volumes (⚠️  DESTRUCTIVE)
	@echo "⚠️  This will remove ALL data volumes!"
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ]
	docker-compose down -v
	docker volume rm jupyterhub_data ollama_data 2>/dev/null || true

clean-images: ## Remove built images
	@echo "Removing built images..."
	docker rmi $(HUB_IMAGE_NAME):$(TAG) $(SINGLEUSER_IMAGE_NAME):$(TAG) 2>/dev/null || true

clean-all: clean clean-volumes clean-images ## Complete cleanup (⚠️  DESTRUCTIVE)

# Registry Operations
push-images: ## Push images to registry
	@echo "Pushing images to $(DOCKER_REGISTRY)..."
	docker tag $(HUB_IMAGE_NAME):$(TAG) $(DOCKER_REGISTRY)/$(HUB_IMAGE_NAME):$(TAG)
	docker tag $(SINGLEUSER_IMAGE_NAME):$(TAG) $(DOCKER_REGISTRY)/$(SINGLEUSER_IMAGE_NAME):$(TAG)
	docker push $(DOCKER_REGISTRY)/$(HUB_IMAGE_NAME):$(TAG)
	docker push $(DOCKER_REGISTRY)/$(SINGLEUSER_IMAGE_NAME):$(TAG)

pull-images: ## Pull images from registry
	@echo "Pulling images from $(DOCKER_REGISTRY)..."
	docker pull $(DOCKER_REGISTRY)/$(HUB_IMAGE_NAME):$(TAG)
	docker pull $(DOCKER_REGISTRY)/$(SINGLEUSER_IMAGE_NAME):$(TAG)
	docker tag $(DOCKER_REGISTRY)/$(HUB_IMAGE_NAME):$(TAG) $(HUB_IMAGE_NAME):$(TAG)
	docker tag $(DOCKER_REGISTRY)/$(SINGLEUSER_IMAGE_NAME):$(TAG) $(SINGLEUSER_IMAGE_NAME):$(TAG)

# Utility Commands
shell-hub: ## Get shell access to JupyterHub container
	docker-compose exec hub bash

update-deps: ## Update Python dependencies in requirements.txt
	@echo "This will rebuild the singleuser image with updated dependencies..."
	@read -p "Continue? (y/N): " confirm && [ "$$confirm" = "y" ]
	docker-compose build --no-cache singleuser

# Show current configuration
show-config: ## Display current configuration
	@echo "Current Configuration:"
	@echo "====================="
	@echo "Hub Image: $(HUB_IMAGE_NAME):$(TAG)"
	@echo "SingleUser Image: $(SINGLEUSER_IMAGE_NAME):$(TAG)"
	@echo "Registry: $(DOCKER_REGISTRY)"
	@echo ""
	@echo "Environment file (ai.env):"
	@if [ -f ai.env ]; then cat ai.env | grep -v "API_KEY" | sed 's/=.*/=****/'; else echo "❌ ai.env not found"; fi
	@echo ""
	@echo "Secret files:"
	@if [ -f secrets/oauth_client_id.txt ]; then echo "✅ oauth_client_id.txt exists"; else echo "❌ oauth_client_id.txt missing"; fi
	@if [ -f secrets/oauth_client_secret.txt ]; then echo "✅ oauth_client_secret.txt exists"; else echo "❌ oauth_client_secret.txt missing"; fi