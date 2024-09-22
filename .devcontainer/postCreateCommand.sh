#!/bin/bash

# install debug tools in devcontainer

# tmux
# TODO: add install commands without super user

# atuin
curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh
sed -e "s/atuin init bash/atuin init bash --disable-up-arrow/" ~/.bashrc -i

# glances
pip install glances[all]
