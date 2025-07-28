import os
from oauthenticator.github import GitHubOAuthenticator

c = get_config()

# setup spawner class
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

# set image
c.DockerSpawner.image = os.environ["DOCKER_JUPYTER_IMAGE"]

# set volumes
c.DockerSpawner.notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR") or "/home/jovyan/work"
c.DockerSpawner.volumes = {
    "jupyterhub-user-{username}": "/home/jovyan/work"
}
#  `{username}` will be expanded to the user's username

# remove contaniers once they are stopped
c.DockerSpawner.remove = True
c.DockerSpawner.start_timeout = 60 * 5  # 5 minutes


# store cookie and server files
# c.JupyterHub.cookie_secret_file = os.environ["COOKIE_SECRET"]
# c.JupyterHub.db_url = os.environ["DB_URL"]

c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

# user notebook resources limits
c.DockerSpawner.mem_limit = '2G'
c.DockerSpawner.cpu_limit = 1
c.DockerSpawner.mem_guarantee = '1G'
c.DockerSpawner.cpu_guarantee = 0.5

# set network
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = os.environ["DOCKER_NETWORK_NAME"]
# 告诉单用户容器去哪儿找 Hub
c.JupyterHub.hub_ip = "jupyterhub-ai"
c.JupyterHub.port = 8000
c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"


        

# setup GitHub OAuth
c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.OAuthenticator.allow_all = True
c.OAuthenticator.oauth_callback_url = "http://localhost:8000/hub/oauth_callback"
# 读取 secret 文件内容
with open('/run/secrets/oauth_client_id', 'r') as f:
    c.GitHubOAuthenticator.client_id = f.read().strip()

with open('/run/secrets/oauth_client_secret', 'r') as f:
    c.GitHubOAuthenticator.client_secret = f.read().strip()


c.DockerSpawner.environment = {
    # 基础 Jupyter 环境变量
    "JUPYTER_ENABLE_LAB": "yes",
    "GRANT_SUDO": "no",
    "CHOWN_HOME": "yes",
    "CHOWN_HOME_OPTS": "-R",
    "NB_UID": "1000",
    "NB_GID": "100",
    # AI 相关环境变量传递给用户容器
    "OPENAI_API_KEY": os.environ.get("OPENAI_API_KEY", ""),
    "OPENAI_API_BASE": os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1"),
    "ANTHROPIC_API_KEY": os.environ.get("ANTHROPIC_API_KEY", ""),
    "ALIYUN_API_KEY": os.environ.get("ALIYUN_API_KEY", ""),
    "ALIYUN_API_BASE": os.environ.get(
        "ALIYUN_API_BASE", "https://dashscope.aliyuncs.com/api/v1"
    ),
    "DEEPSEEK_API_KEY": os.environ.get("DEEPSEEK_API_KEY", ""),
    "DEEPSEEK_API_BASE": os.environ.get(
        "DEEPSEEK_API_BASE", "https://api.deepseek.com/v1"
    ),
    # "OLLAMA_API_BASE": os.environ.get("OLLAMA_API_BASE", "http://172.18.0.1:11434"),
    # "OLLAMA_API_KEY": os.environ.get("OLLAMA_API_KEY", "ollama"),
    'OLLAMA_URL': 'http://ollama:11434'
    # "AI_PROXY_URL": os.environ.get("AI_PROXY_URL", "http://ip:8080"),
    # "USE_AI_PROXY": os.environ.get("USE_AI_PROXY", "true"),
}