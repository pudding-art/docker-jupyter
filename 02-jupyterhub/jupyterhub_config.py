import os

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

# resources limits
c.DockerSpawner.mem_limit = '1G'
c.DockerSpawner.cpu_limit = 0.5


# set network
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = os.environ["DOCKER_NETWORK_NAME"]
# 告诉单用户容器去哪儿找 Hub
c.JupyterHub.hub_ip = "jupyterhub"
c.JupyterHub.port = 8000

c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"



# Allow all signed-up users to login
c.JupyterHub.authenticator_class = "jupyterhub.auth.DummyAuthenticator"
c.Authenticator.allow_all = True             

