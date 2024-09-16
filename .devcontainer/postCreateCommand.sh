#!/bin/bash

# install debug tools in devcontainer

# tmux
# TODO: add install commands without super user
settings_json="${HOME}/.vscode-server/data/Machine/settings.json"
touch $settings_json
echo -e "{\n    \"terminal.integrated.defaultProfile.linux\": \"tmux\"\n}" >> $settings_json

# atuin
curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh
sed -e "s/atuin init bash/atuin init bash --disable-up-arrow/" ~/.bashrc -i

# glances
pip install glances[all]
