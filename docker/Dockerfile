FROM ubuntu:20.04

ARG USERNAME="developer"
ARG GROUPNAME="developer"
ARG UID=1000
ARG GID=1000
ARG WORKDIR="/workspace"


# Basic packages
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    vim \
    tmux \
    less \
    tree \
    git \
    wget \
    unzip \
    openssh-client \
    pkg-config \
    gdb \
    clangd \
    cmake \
    ninja-build

# Python packages
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    python3.8 \
    python3-pip \
    python-is-python3

# install python module
RUN pip install --upgrade pip
COPY . ${WORKDIR}
RUN pip install --no-cache-dir -e ${WORKDIR}[dev,test]

# Modify authority
RUN groupadd -g ${GID} ${GROUPNAME} \
    && useradd -m -s /bin/bash -u ${UID} -g ${GID} ${GROUPNAME}
WORKDIR ${WORKDIR}
RUN chown -R ${USERNAME}:${GROUPNAME} ${WORKDIR}
USER ${USERNAME}
