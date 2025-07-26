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
c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

# resources limits
c.DockerSpawner.mem_limit = '1G'
c.DockerSpawner.cpu_limit = 0.5

# set network
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = os.environ["DOCKER_NETWORK_NAME"]
# 告诉单用户容器去哪儿找 Hub
c.JupyterHub.hub_ip = "jupyterhub"
c.JupyterHub.port = 8000

# Allow all signed-up users to login
# c.JupyterHub.authenticator_class = "jupyterhub.auth.DummyAuthenticator"
# c.Authenticator.allow_all = True             

# setup GitHub OAuth
# c.JupyterHub.authenticator_class = "github"
c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.OAuthenticator.allow_all = True
c.OAuthenticator.oauth_callback_url = "http://localhost:8000/hub/oauth_callback"
# c.OAuthenticator.client_id = os.environ["OAUTH_CLIENT_ID"]
# c.OAuthenticator.client_secret = os.environ["OAUTH_CLIENT_SECRET"]
# 读取 secret 文件内容
with open('/run/secrets/oauth_client_id', 'r') as f:
    c.GitHubOAuthenticator.client_id = f.read().strip()

with open('/run/secrets/oauth_client_secret', 'r') as f:
    c.GitHubOAuthenticator.client_secret = f.read().strip()
