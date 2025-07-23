FROM  quay.io/jupyter/scipy-notebook:ubuntu-24.04


USER root 
# udpate the base image to ensure we have the latest packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# copy essential files
COPY notebooks /home/$NB_USER/notebooks
COPY data /home/$NB_USER/data

# configure jupyter configuration
RUN chown -R $NB_UID:$NB_GID /home/$NB_USER/.jupyter &&\
    fix-permissions "/home/${NB_USER}"


# install python packages
USER $NB_USER
COPY  ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt


EXPOSE 8888