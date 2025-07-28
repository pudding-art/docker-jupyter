## 使用教程

拿 key → 装插件 → 插件帮你实时调用各家大模型 → Notebook/聊天界面里即刻拿到回答

python版本最好3.12，下载jupyterlab和notebook
```shell
pip install jupyterlab
pip install notebook
```

创建一个jupyter-ai的conda环境：
```shell
conda create -n jupyter-ai python=3.12 jupyterlab
```

同时安装%%aimagic 和 JupyterLab 扩展：

```shell
conda create -n jupyter-ai python=3.12 jupyterlab
conda activate jupyter-ai
pip install 'jupyter-ai[all]'
```

启动Jupyterlab：
```shell
jupyter lab

(jupyter-ai) ➜  04-jupyterhub-ai-enhanced git:(main) ✗ jupyter lab                  
[I 2025-07-26 18:05:23.165 ServerApp] jupyter_ai | extension was successfully linked.
[I 2025-07-26 18:05:23.166 ServerApp] jupyter_lsp | extension was successfully linked.
[I 2025-07-26 18:05:23.169 ServerApp] jupyter_server_terminals | extension was successfully linked.
[I 2025-07-26 18:05:23.174 ServerApp] jupyterlab | extension was successfully linked.
[W 2025-07-26 18:05:23.177 JupyterNotebookApp] 'iopub_data_rate_limit' has moved from NotebookApp to ServerApp. This config will be passed to ServerApp. Be sure to update your config before our next release.
[W 2025-07-26 18:05:23.180 ServerApp] ServerApp.iopub_data_rate_limit config is deprecated in 2.0. Use ZMQChannelsWebsocketConnection.iopub_data_rate_limit.
[I 2025-07-26 18:05:23.180 ServerApp] notebook | extension was successfully linked.
[I 2025-07-26 18:05:23.404 ServerApp] notebook_shim | extension was successfully linked.
[I 2025-07-26 18:05:23.449 ServerApp] notebook_shim | extension was successfully loaded.
[I 2025-07-26 18:05:23.450 AiExtension] Configured provider allowlist: None
[I 2025-07-26 18:05:23.450 AiExtension] Configured provider blocklist: None
[I 2025-07-26 18:05:23.450 AiExtension] Configured model allowlist: None
[I 2025-07-26 18:05:23.450 AiExtension] Configured model blocklist: None
[I 2025-07-26 18:05:23.450 AiExtension] Configured model parameters: {}
[I 2025-07-26 18:05:23.468 AiExtension] Registered model provider `ai21`.
[I 2025-07-26 18:05:23.599 AiExtension] Registered model provider `bedrock`.
[I 2025-07-26 18:05:23.599 AiExtension] Registered model provider `bedrock-chat`.
[I 2025-07-26 18:05:23.599 AiExtension] Registered model provider `bedrock-custom`.
[I 2025-07-26 18:05:23.874 AiExtension] Registered model provider `anthropic-chat`.
[I 2025-07-26 18:05:24.484 AiExtension] Registered model provider `azure-chat-openai`.
[I 2025-07-26 18:05:27.480 AiExtension] Registered model provider `cohere`.
[I 2025-07-26 18:05:28.539 AiExtension] Registered model provider `gemini`.
[I 2025-07-26 18:05:28.539 AiExtension] Registered model provider `gpt4all`.
[I 2025-07-26 18:05:28.540 AiExtension] Registered model provider `huggingface_hub`.
[I 2025-07-26 18:05:28.585 AiExtension] Registered model provider `mistralai`.
[I 2025-07-26 18:05:28.609 AiExtension] Registered model provider `nvidia-chat`.
[I 2025-07-26 18:05:28.792 AiExtension] Registered model provider `ollama`.
[I 2025-07-26 18:05:28.793 AiExtension] Registered model provider `openai`.
[I 2025-07-26 18:05:28.793 AiExtension] Registered model provider `openai-chat`.
[I 2025-07-26 18:05:28.793 AiExtension] Registered model provider `openai-chat-custom`.
[I 2025-07-26 18:05:28.807 AiExtension] Registered model provider `openrouter`.
[I 2025-07-26 18:05:28.807 AiExtension] Registered model provider `qianfan`.
[I 2025-07-26 18:05:28.807 AiExtension] Registered model provider `sagemaker-endpoint`.
[I 2025-07-26 18:05:28.807 AiExtension] Registered model provider `togetherai`.
[I 2025-07-26 18:05:37.909 AiExtension] Registered model provider `vertexai`.
[I 2025-07-26 18:05:37.928 AiExtension] Registered embeddings model provider `azure`.
[I 2025-07-26 18:05:37.928 AiExtension] Registered embeddings model provider `bedrock`.
[I 2025-07-26 18:05:37.928 AiExtension] Registered embeddings model provider `cohere`.
[I 2025-07-26 18:05:37.928 AiExtension] Registered embeddings model provider `gpt4all`.
[I 2025-07-26 18:05:37.928 AiExtension] Registered embeddings model provider `huggingface_hub`.
[I 2025-07-26 18:05:37.928 AiExtension] Registered embeddings model provider `mistralai`.
[I 2025-07-26 18:05:37.928 AiExtension] Registered embeddings model provider `ollama`.
[I 2025-07-26 18:05:37.928 AiExtension] Registered embeddings model provider `openai`.
[I 2025-07-26 18:05:37.928 AiExtension] Registered embeddings model provider `openai-custom`.
[I 2025-07-26 18:05:37.928 AiExtension] Registered embeddings model provider `qianfan`.
[I 2025-07-26 18:05:37.928 AiExtension] Registered embeddings model provider `vertexai`.
[I 2025-07-26 18:05:37.939 AiExtension] Registered providers.
[I 2025-07-26 18:05:37.939 AiExtension] Registered jupyter_ai server extension
[I 2025-07-26 18:05:37.961 AiExtension] Registered chat handler `ask` with command `/ask`.
[I 2025-07-26 18:05:37.962 AiExtension] Registered chat handler `clear` with command `/clear`.
[I 2025-07-26 18:05:37.962 AiExtension] Registered chat handler `default` with command `default`.
[I 2025-07-26 18:05:37.962 AiExtension] Registered chat handler `export` with command `/export`.
[I 2025-07-26 18:05:37.963 AiExtension] Registered chat handler `fix` with command `/fix`.
[I 2025-07-26 18:05:37.963 AiExtension] Registered chat handler `generate` with command `/generate`.
[I 2025-07-26 18:05:37.963 AiExtension] Registered chat handler `help` with command `/help`.
[I 2025-07-26 18:05:37.964 AiExtension] Registered chat handler `learn` with command `/learn`.
[I 2025-07-26 18:05:37.980 AiExtension] Registered context provider `file`.
[I 2025-07-26 18:05:37.982 AiExtension] Initialized Jupyter AI server extension in 14532 ms.
[I 2025-07-26 18:05:37.983 ServerApp] jupyter_ai | extension was successfully loaded.
[I 2025-07-26 18:05:37.985 ServerApp] jupyter_lsp | extension was successfully loaded.
[I 2025-07-26 18:05:37.986 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2025-07-26 18:05:37.991 LabApp] JupyterLab extension loaded from /Users/hong/opt/anaconda3/envs/hta_new/lib/python3.9/site-packages/jupyterlab
[I 2025-07-26 18:05:37.991 LabApp] JupyterLab application directory is /Users/hong/opt/anaconda3/envs/hta_new/share/jupyter/lab
[I 2025-07-26 18:05:37.992 LabApp] Extension Manager is 'pypi'.
[I 2025-07-26 18:05:38.102 ServerApp] jupyterlab | extension was successfully loaded.
[I 2025-07-26 18:05:38.106 ServerApp] notebook | extension was successfully loaded.
[I 2025-07-26 18:05:38.107 ServerApp] Serving notebooks from local directory: /Users/hong/docker-jupyter/04-jupyterhub-ai-enhanced
[I 2025-07-26 18:05:38.107 ServerApp] Jupyter Server 2.16.0 is running at:
[I 2025-07-26 18:05:38.107 ServerApp] http://localhost:8888/lab?token=c3ec2b0224eb434df1eeabfc24f797023bb41e638406bc83
[I 2025-07-26 18:05:38.107 ServerApp]     http://127.0.0.1:8888/lab?token=c3ec2b0224eb434df1eeabfc24f797023bb41e638406bc83
[I 2025-07-26 18:05:38.107 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2025-07-26 18:05:38.128 ServerApp] 
    
    To access the server, open this file in a browser:
        file:///Users/hong/Library/Jupyter/runtime/jpserver-64335-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/lab?token=c3ec2b0224eb434df1eeabfc24f797023bb41e638406bc83
        http://127.0.0.1:8888/lab?token=c3ec2b0224eb434df1eeabfc24f797023bb41e638406bc83
```


pip install deepseek 只是把 DeepSeek 官方 SDK 装进来（一个 Python 包，让你能 import deepseek）。
而 pip install -e /opt/ai-providers 是把 我们自己写的“Jupyter-AI Provider 插件” 安装到 JupyterLab 的入口点（entry point），让 %%ai deepseek:xxx 魔法命令能在 UI 里出现、在 Notebook 里被识别。




应对网络问题有三种方法：
1. 使用国内的AI模型
2. 使用代理
3. ollama本地部署

使用国内的AI代理直接去官网拿API key即可，使用代理需要设置`AI_PROXY_URL`和`USE_AI_PROXY`,ollama本地部署需要创建另一个ollama镜像，在Notebook里写码时通过内部网络访问ollama容器接口，由network连接。

API需要在docker.singleuser中pip install对应的包即可，然后docker-compose.yml文件中之需要修改env环境变量文件，jupyterhub_config.py文件中，需要使用c.DockerSpawner.environments将包括API key和API base的环境变量设置一下，将环境变量传入到spawner创建的容器中，然后容器中已经install了对应厂商的ai package，直接调用即可。


网页版AI和API区别

1. 成本结构不同
- 网页版：厂商自己把控对话长度、并发数，平均成本低；再加上前端广告、品牌溢价，亏得起。
- API：开发者想跑多大流量就跑多大流量，每 1 个 token 都是 GPU 显存和电费，成本实打实 。
2. 商业目标不同
- 网页版 = 获客工具。用“免费尝鲜”拉来海量 C 端用户，收集数据、训练下一代模型，再推订阅（如 ChatGPT Plus）或广告 。
- API = 盈利工具。开发者或企业把能力嵌进自家产品，按调用量付费，这是目前最清晰的现金流 。
3. 风险敞口不同
- 网页版：厂商可以“限速”“限次数”，甚至插广告，把滥用压到最低。
- API：一旦开放，就可能被刷爆；于是厂商用“预充值+按量计费”把风险转嫁给调用方 。
所以，你在浏览器里聊得再嗨，也只是厂商“市场费用”的一部分；一旦通过 API 把模型搬到自己程序里，就要为它真正的算力成本买单。



### ollama方法

 在 Notebook 容器中使用 Ollama 服务
在 Notebook 容器中，你可以通过这些环境变量来访问 Ollama 服务。例如，你可以使用 requests 库来调用 Ollama API：
```Python
import os
import requests

# 获取环境变量
ollama_api_base = os.environ.get("OLLAMA_API_BASE")
ollama_api_key = os.environ.get("OLLAMA_API_KEY")
ollama_url = os.environ.get("OLLAMA_URL")

# 示例：调用 Ollama API 查询模型信息
headers = {
    "Authorization": f"Bearer {ollama_api_key}"
}
response = requests.get(f"{ollama_api_base}/api/models", headers=headers)

print(response.json())
```

### postgresql

在 JupyterHub 中使用 PostgreSQL 时，通常会将与用户和用户会话相关的一些数据存储到 PostgreSQL 数据库中。这些数据可能包括：用户信息,用户名,密码（通常以加密形式存储）,用户属性（如邮箱、昵称等）;用户会话信息：用户的登录记录,用户的会话状态（如会话开始时间、结束时间等）;服务器配置：JupyterHub 的配置参数,用户的个性化设置;其他自定义数据：其他自定义数据，例如课程信息、项目信息等。

增加postgresql持久化功能，docker-compose.yml增加如下内容：

```shell
  postgres:
    image: postgres:latest # 使用官方 postgres 镜像
    container_name: postgresql
    profiles:
      - default
    networks:
      - jupyterhub-network
    ports:
      - "5432:5432"  # PostgreSQL 默认端口
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: mysecretpassword
      POSTGRES_DB: jupyterhub_db
    volumes:
      - postgres_data:/var/lib/postgresql/data  # 数据持久化卷
    restart: unless-stopped

```

设置了环境变量 POSTGRES_USER、POSTGRES_PASSWORD 和 POSTGRES_DB，分别用于定义默认用户、密码和数据库名称。数据持久化通过挂载 Docker 卷 postgres_data 到容器内的 /var/lib/postgresql/data 目录实现，确保即使容器被删除，数据也不会丢失。PostgreSQL 服务与 JupyterHub 和 Ollama 服务共享同一个网络 jupyterhub-network，确保它们可以相互通信。PostgreSQL 的默认端口 5432 被映射到宿主机的 5432 端口，便于从宿主机访问数据库。
设置了 restart: unless-stopped，确保 PostgreSQL 服务在容器退出后自动重启。


jupyterhub_config.py中需要配置配置 JupyterHub 使用 PostgreSQL 作为用户数据库。
```python
c.JupyterHub.db_url = 'postgresql://postgres:mysecretpassword@localhost:5432/jupyterhub_db'`
```


在 JupyterHub 中创建一个用户，然后使用以下 SQL 查询检查 PostgreSQL 数据库中的 users 表：
```sql
SELECT * FROM users;
```