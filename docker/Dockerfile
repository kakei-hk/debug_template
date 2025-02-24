FROM ubuntu:22.04

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
    lsb-release \
    software-properties-common \
    gpg-agent \
    ninja-build

# Specific version CMake
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc | apt-key add - \
    && apt-add-repository "deb https://apt.kitware.com/ubuntu/ $(lsb_release -cs) main" \
    && apt-get update && apt-get install -y cmake-data=3.29.6-0kitware1ubuntu22.04.1 cmake=3.29.6-0kitware1ubuntu22.04.1

# Python packages
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    python3.10 \
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
