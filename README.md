# argapp - A Python package for CLI application development

# Overview

argapp is an OOP wrapper for [argparse](https://docs.python.org/3/library/argparse.html) and [argcomplete](https://pypi.org/project/argcomplete):
 * Allows writing CLI applications using OOP - encapsulates argparse API.
 * Optionally supports shell completion via argcomplete - encapsulates its API.

## Features

 * Offers several classes that allow building a Python CLI application in OOP style.
    * `Arg` represents optional and positional arguments, with the most essential use cases covered.
    * `App` represents a main appplication or a sub-command.
    * Instances of the classes are immutable.
    * The fields are validated upon construction, raising an `Exception` in case of any issues.
    * The command line parsing can be overridden to return custom values for a specific `Arg`.
 * Offers shell completion support if argcomplete is installed:
    * The required API calls are already in place. It is only required to install argcomplete and add the `PYTHON_ARGCOMPLETE_OK` comment.
    * Specific completions (like from choices) are added automatically.

## Dependencies

 * Linux
 * Python 3
    * 3.6
    * 3.7
    * 3.8
    * 3.9
    * 3.10
    * 3.11

## Limitations

 * No "required" optional arguments.
 * No value aggregation (like for compilation flags).
 * No argument groups of any kind.
 * Choices are restrictive (cannot be disabled).
 * Completions cannot be customized.

# Installation

 * The package can be installed globally by running:
   ```shell
   pip3 install argapp
   ```
 * The Git [repository](https://github.com/deohayer/argapp) can be used directly if a specific version is needed.<br>
   The repository layout is designed with exactly this use case in mind.
 * For the argcomplete installation, please follow the official [documentation](https://pypi.org/project/argcomplete).

# API
