FROM quay.io/jupyterhub/jupyterhub:latest

USER root
RUN python3 -m pip install --no-cache-dir \
    dockerspawner \
    oauthenticator
    # jupyterhub-dummyauthenticator 

    
# CMD ["jupyterhub","--config","/srv/jupyterhub/jupyterhub_config.py"]



