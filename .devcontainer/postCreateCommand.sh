#!/bin/bash

# additionally install tools in devcontainer here if you don't want to change base Docker image

# atuin
curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh
sed -e "s/atuin init bash/atuin init bash --disable-up-arrow/" ~/.bashrc -i

# glances
pip install glances[all]
