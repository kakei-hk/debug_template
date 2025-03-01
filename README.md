# Debug Template

## Overview

This repository provides simple debug environment with VScode extensions.

## How to Use

### Prepare Docker Image and Dev Container

`Dev Containers` is a VScode extension which enables you to debug your code with VScode debug extensions in docker container.
You can prepare Dev Container with the following steps.

- Install docker and `Dev Containers`(ID:ms-vscode-remote.remote-containers) extension into VScode in your host PC.
- (optional) Modify `.devcontainer/devcontainer.json`, `.devcontainer/postCreateCommand.sh` for your environment or preferences.
- Build docker image by executing `./docker/docker_build.sh`.
- Open command palette with `Ctrl + Shift + P` and select `Dev Containers: Rebuild and Reopen in Container` for the first build or container update.
  - If you want to just reopen Dev Container without rebuild or update, `Dev Containers: Reopen in Container` is available.

### Debug Examples with VScode Extensions

#### Python Debug Example

This project provides an example Python package, `pydebug_template`, to show how you can develop your Python project with devcontainer.

The following points are important to debug Python code.

- `Python` extension (ID:ms-python.python) provides fundamental features for debug.
- `launch.json` enables you to configure how you run and debug your Python code.
  - Reference configurations with type `debugpy` in `.vscode/launch.json`.
- `settings.json` enables you to set autocomplete, linter and so on.
  - Reference settings in `.vscode/settings.json`.

You can debug `pydebug_template/example/example.py` with the following steps.

- (optional) Check codes in pydebug_template/ and add breakpoint (press `F9` at where you want to stop).
- Open `Debug and Run` with `Ctrl + Shift + D` and select `Python: run example script` (configuration name in `launch.json`).
- Run debug with `F5`.

#### C/C++ Debug Example

`cppdebug_template` demonstrates how you can build and debug C/C++ program.

As similar to Python debug, the following points are important for C/C++ debug.

- `C/C++` extension (ID:ms-vscode.cpptools) provides fundamental features for debug.
- Your code should be built through VScode features so that you can debug with VScode, which will be demonstrated in some examples later.
- `launch.json` enables you to configure how you run and debug your C/C++ code.
  - Reference configurations with type `cppdbg` in `.vscode/launch.json`.
- `settings.json` enables you to set autocomplete, linter and so on.
  - Reference settings in `.vscode/settings.json`.
  - In the `settings.json` in this project, `clangd`(ID:llvm-vs-code-extensions.vscode-clangd) is adopted for the code intellisense and some `C/C++` extension intellisense should be disabled due to conflicting.
  - Note that `clangd` in this project makes use of `compile_commands.json`, which is created after CMake configuration explained later.

`cppdebug_template` has two types of examples depending on the way to build the codes. The following sections explain how to build and debug each example.

##### Build with tasks.json

One way to build C/C++ code is to describe compile command in `tasks.json` (reference `.vscode/tasks.json`). It helps you configure simple project build.
`cppdebug_template` provides quite simple hello world example (`cppdebug_template/hello_world/hello_world.cpp`), which can be built through `.vscode/tasks.json`.
How to build and debug hello world example is as follows.

- Open `cppdebug_template/hello_world/hello_world.cpp`.
- Press `Ctrl + Shift + B` or select `Tasks: Run Build Task` in command palette to build hello_world.cpp.
- (optional) Check code and add breakpoint (press `F9` at where you want to stop).
- Open `Debug and Run` with `Ctrl + Shift + D` and select `C/C++: Current File` (configuration name in `launch.json`).
- Run debug with `F5`.

##### Build with CMake Tools Extension

As your project becomes complicated, CMake helps you configure the project. VScode provides `CMake Tools` extension (ID:ms-vscode.cmake-tools), which enables you to notify VScode of your CMake configuration and to build and debug the project.
`cppdebug_template` has CMake build example. Note that this example uses `CMakePresets.json`, which is available with 3.19 or later version of CMake and able to set multiple configurations separate from `CMakeLists.txt`.
`CMake Tools` can load `CMakePresets.json` and configure the project through it.

The build and debug with CMake in this example is as follows.

- Open command palette with `Ctrl + Shift + P` and select `CMake: Select Configure Preset`.
- Select `debug` (preset name in `cppdebug_template/CMakePresets.json`).
- Open command palette and select `CMake: configure` to run CMake.
- Select `CMake: Build` in command palette or press `F7` to build the example.
- (optional) Check code and add breakpoint (press `F9` at where you want to stop).
- Open `Debug and Run` with `Ctrl + Shift + D` and select `C/C++: debug cppdebug_template example` (configuration name in `launch.json`).
- Run debug with `F5`.
