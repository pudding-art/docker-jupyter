# JupyterHub AI Platform

一个集成了多种 AI 服务的企业级 JupyterHub 平台，支持 GitHub OAuth 认证、Docker 容器化部署，以及包括 OpenAI、Anthropic、阿里云、DeepSeek 和 Ollama 在内的多种 AI 模型集成。

## 🚀 特性

- **多用户支持**: 基于 JupyterHub 的多用户 Jupyter 环境
- **GitHub OAuth**: 安全的 GitHub 身份认证
- **AI 集成**: 内置 Jupyter-AI 扩展，支持多种 AI 提供商
- **容器化部署**: 完全基于 Docker 的部署方案
- **资源管理**: 容器级别的 CPU 和内存限制
- **持久化存储**: 用户数据和配置的持久化存储
- **本地 AI**: 集成 Ollama 支持本地大模型推理

## 🏗️ 架构概览

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   GitHub OAuth  │    │   JupyterHub     │    │   User Jupyter  │
│   认证服务       │◄──►│   主服务         │◄──►│   容器实例       │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │                         │
                              ▼                         ▼
                       ┌──────────────┐         ┌─────────────────┐
                       │   Docker     │         │   AI Services   │
                       │   网络和存储  │         │   集成          │
                       └──────────────┘         └─────────────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │     Ollama      │
                                               │   本地AI模型    │
                                               └─────────────────┘
```

## 📋 系统要求

- Docker Engine 20.10+
- Docker Compose v2.0+
- 至少 4GB 可用内存
- 至少 10GB 可用磁盘空间
- 支持的操作系统: Linux, macOS, Windows (WSL2)

## 🛠️ 快速开始

### 1. 克隆项目

```bash
git clone <repository-url>
cd jupyterhub-ai
```

### 2. 初始化项目

```bash
make setup
```

这将创建必要的目录结构和模板配置文件。

### 3. 配置 GitHub OAuth

1. 前往 [GitHub Developer Settings](https://github.com/settings/developers)
2. 创建新的 OAuth App
3. 设置 Authorization callback URL: `http://localhost:8000/hub/oauth_callback`
4. 将 Client ID 和 Client Secret 分别保存到：
   - `secrets/oauth_client_id.txt`
   - `secrets/oauth_client_secret.txt`

### 4. 配置 AI API 密钥

编辑 `ai.env` 文件，填入您的 AI 服务 API 密钥：

```bash
# 必填：至少配置一个 AI 服务
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
ALIYUN_API_KEY=your_aliyun_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key
```

### 5. 构建和启动

```bash
# 构建所有镜像
make build

# 启动服务（不包含 Ollama）
make start

# 或者启动包含 Ollama 的完整服务
make start-with-ollama
```

### 6. 访问服务

- **JupyterHub**: http://localhost:8000
- **Ollama API** (如果启用): http://localhost:11434

## 📖 使用指南

### Makefile 命令参考

#### 设置和配置
```bash
make setup           # 初始化项目（创建目录和模板文件）
make setup-dirs      # 创建必要目录
make setup-secrets   # 创建密钥模板文件
make setup-env      # 创建环境变量模板文件
```

#### 构建命令
```bash
make build          # 构建所有 Docker 镜像
make build-hub      # 只构建 JupyterHub 镜像
make build-singleuser # 只构建单用户 Jupyter 镜像
```

#### 服务管理
```bash
make start          # 启动服务（默认配置）
make start-with-ollama # 启动包含 Ollama 的完整服务
make stop           # 停止所有服务
make restart        # 重启所有服务
make dev-start      # 开发模式启动（自动构建）
```

#### Ollama 管理
```bash
make ollama-start              # 启动 Ollama 服务
make ollama-stop               # 停止 Ollama 服务
make ollama-pull MODEL=llama2  # 拉取指定模型
make ollama-list               # 列出已安装模型
```

#### 监控和日志
```bash
make status         # 显示服务状态
make logs          # 显示所有服务日志
make logs-hub      # 显示 JupyterHub 日志
make logs-ollama   # 显示 Ollama 日志
make health-check  # 检查服务健康状态
```

#### 数据管理
```bash
make backup        # 备份数据
make restore BACKUP_DIR=20240101_120000 # 从备份恢复
```

#### 清理命令
```bash
make clean         # 停止服务并删除容器
make clean-volumes # 删除所有数据卷（⚠️ 危险操作）
make clean-images  # 删除构建的镜像
make clean-all     # 完全清理（⚠️ 危险操作）
```

### 在 Jupyter 中使用 AI

启动成功后，在 Jupyter Notebook 中可以使用以下魔法命令：

#### OpenAI
```python
%%ai openai-chat:gpt-4
你好，请帮我解释一下机器学习的基本概念。
```

#### Anthropic Claude
```python
%%ai anthropic-chat:claude-3-sonnet
请写一个 Python 函数来计算斐波那契数列。
```

#### 阿里云通义千问
```python
%%ai qianwen-chat
帮我分析这个数据集的统计特征。
```

#### Ollama 本地模型
```python
%%ai ollama-chat:llama2  # 需要先拉取模型
解释量子计算的基本原理。
```

### 配置文件详解

#### docker-compose.yml
- **hub 服务**: JupyterHub 主服务，处理认证和用户管理
- **ollama 服务**: 本地 AI 模型推理服务
- **网络配置**: 内部 Docker 网络用于服务间通信
- **卷挂载**: 持久化存储用户数据和配置

#### jupyterhub_config.py
主要配置项：
- **DockerSpawner**: 为每个用户启动独立的 Docker 容器
- **资源限制**: CPU 和内存限制配置
- **GitHub OAuth**: 身份认证配置
- **环境变量传递**: 将 AI API 密钥传递给用户容器

#### Dockerfile.singleuser
单用户容器包含：
- Jupyter Lab 和相关扩展
- Python 科学计算栈 (pandas, numpy, scikit-learn 等)
- AI 工具 (transformers, langchain, jupyter-ai 等)
- 开发工具 (git, vim, language servers 等)

## 🔧 自定义配置

### 添加新的 AI 提供商

1. 在 `requirements.txt` 中添加相应的客户端库
2. 在 `jupyterhub_config.py` 中添加环境变量配置
3. 在 `ai.env` 中添加 API 密钥配置
4. 重新构建单用户镜像

### 修改资源限制

在 `jupyterhub_config.py` 中调整：
```python
c.DockerSpawner.mem_limit = '4G'      # 内存限制
c.DockerSpawner.cpu_limit = 2         # CPU 限制
c.DockerSpawner.mem_guarantee = '2G'  # 内存保证
c.DockerSpawner.cpu_guarantee = 1     # CPU 保证
```

### 添加自定义 Python 包

在 `requirements.txt` 中添加所需包，然后重新构建：
```bash
make build-singleuser
```

## 🚨 故障排除

### 常见问题

#### 1. 容器启动失败
```bash
# 检查日志
make logs

# 检查 Docker 资源
docker system df
docker system prune  # 清理未使用的资源
```

#### 2. GitHub OAuth 认证失败
- 检查 `secrets/` 目录下的文件内容
- 确认 GitHub OAuth App 的回调 URL 配置正确
- 检查防火墙和网络连接

#### 3. AI API 调用失败
```bash
# 检查环境变量
make show-config

# 测试 API 连通性
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.openai.com/v1/models
```

#### 4. Ollama 模型加载失败
```bash
# 检查 Ollama 服务状态
make ollama-list

# 手动拉取模型
make ollama-pull MODEL=llama2

# 检查磁盘空间
df -h
```

### 性能优化

#### 1. 容器预热
```bash
# 预先拉取基础镜像
docker pull quay.io/jupyter/base-notebook:python-3.11
docker pull ollama/ollama:latest
```

#### 2. 网络优化
```bash
# 使用本地镜像仓库
export DOCKER_REGISTRY=your-registry.com
make push-images
```

#### 3. 存储优化
```bash
# 定期清理未使用的容器和镜像
docker system prune -a

# 定期备份数据
make backup
```

## 🔒 安全考虑

### 生产环境部署

1. **使用 HTTPS**: 配置 SSL/TLS 证书
2. **网络隔离**: 使用防火墙限制网络访问
3. **定期更新**: 保持 Docker 镜像和依赖包最新
4. **日志监控**: 设置日志收集和监控
5. **备份策略**: 制定定期备份计划

### API 密钥管理

- 使用环境变量而非硬编码
- 定期轮换 API 密钥
- 限制 API 密钥权限范围
- 监控 API 使用情况

## 📝 开发和贡献

### 开发环境设置

```bash
# 克隆仓库
git clone <repository-url>
cd jupyterhub-ai

# 设置开发环境
make setup
make dev-start

# 查看日志
make logs
```

### 项目结构

```
├── Dockerfile.jupyterhub     # JupyterHub 服务 Dockerfile
├── Dockerfile.singleuser     # 单用户容器 Dockerfile
├── docker-compose.yml        # Docker Compose 配置
├── jupyterhub_config.py      # JupyterHub 配置文件
├── requirements.txt          # Python 依赖
├── Makefile                  # 构建和管理脚本
├── ai.env                    # 环境变量配置
├── secrets/                  # OAuth 密钥文件
│   ├── oauth_client_id.txt
│   └── oauth_client_secret.txt
├── examples/                 # 示例 Jupyter Notebooks
├── backup/                   # 备份文件
└── README.md                 # 项目文档
```

## 📄 许可证

本项目基于 MIT 许可证开源。详细信息请查看 LICENSE 文件。

## 🆘 支持

如果您遇到问题或有功能建议，请：

1. 查看故障排除部分
2. 检查现有的 GitHub Issues
3. 创建新的 Issue 并提供详细信息
4. 参与社区讨论

## 🙏 致谢

感谢以下开源项目：

- [JupyterHub](https://github.com/jupyterhub/jupyterhub)
- [Jupyter AI](https://github.com/jupyterlab/jupyter-ai)
- [Ollama](https://github.com/ollama/ollama)
- [LangChain](https://github.com/langchain-ai/langchain)

---

**快速开始**: `make setup && make build && make start`

**获取帮助**: `make help`