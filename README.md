# Debug Template

## Overview

This repository provides simple debug environment with devcontainer.

## How to Use

### Prepare docker image and container

1. (optional) Modify `.devcontainer/devcontainer.json`, `.devcontainer/postCreateCommand.sh` for your environment.
2. Build docker image by executing `./docker/docker_build.sh`.
3. Build and open devcontainer using the build docker image.

### Run Python sample program

- This project provides an example Python package, `pydebug_template`, to show how you can develop your Python project with devcontainer.
- You can run a sample program from `Run and Debug` of VScode side bar according to the debug setting in `.vscode/launch.json`. Besides, you can learn how VScode auto format or highlight feature specified in `.vscode/settings.json` works by editing the sample code.
