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

## `argapp`

The package is the module by itself. It only exports its classes to not pollute the namespace.

### Example: Hello, world!

Below is `argapp.py` which prints a hello message with the given argument.

```python
#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

from argapp import Arg, App


class ExampleApp(App):  # Inherit App to override the construction and the runtime.
    def __init__(self) -> None:
        super().__init__(help='A minimalistic App.', epilog='Bottom text.')
        # Define a positional argument.
        self.arg = Arg(app=self,         # This is mandatory, adds Arg to App.
                       count='?',        # Make this argument non-required.
                       default='world',  # Provide a default value.
                       name='WHO')       # Provide a unique name (for the help message).

    def __call__(
        self,
        args: dict[Arg] = None,
        apps: list[App] = None,
    ) -> None:
        # A mandatory call to super(). The default implementation:
        #  * Parses the raw command line to populate args and apps.
        #  * Calls this method again with args and apps properly set.
        super().__call__(args, apps)
        # Retrieve the value using self.arg as the key, and print the message:
        print(f'Hello, {args[self.arg]}!')


# Construct and call.
ExampleApp()()
```

The help:

```shell
./argapp.py -h
# The output:
argapp.py [WHO]

A minimalistic App.

positional arguments:
  WHO    Defaults to: world

optional arguments:
  -h, --help     Show the help message and exit.

Bottom text.
```

The usage:

```shell
# No argument.
./argapp.py
# self.arg defaults to "world":
Hello, world!

#--------------------------------------------------------

# With argument.
./argapp.py John
# self.arg is "John":
Hello, John!
```

The completion:

```shell
./argapp.py -
# Upon pressing TAB, the following is displayed:
-h      --help
```

### `Arg`

Represents a command line argument, optional or positional.

A constructed instance is:
 * Added to a certain `App.args` as one of its command line arguments.
 * Used as a key in the dictionary `args` in `App.__call__`.

The fields:
 * Are read-only and can be set once, via `Arg.__init__`.
 * Are validated during `Arg.__init__`.
 * May depend on other fields.

#### Declaration

```python
class Arg:
    ...
```

#### Example

There are several best practices to follow:
 * Sub-class `Arg` to customize the construction or parsing.
 * Create `Arg` instances inside the `App` that will contain it (that is, in `App.__init__`).
 * Save the created `Arg` into an `App` field. In the dictionary of parsed values, `Arg` itself is the key, not its name.

Below is `argapp.py` which adds two integer values and prints the result.

```python
#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

from argapp import Arg, App


class ExampleArg(Arg):
    def __init__(self, app: App, name: str) -> None:
        # Encapsulate the construction.
        # Note that type is set to int for automatic conversion.
        super().__init__(app=app,
                         name=name,
                         type=int,
                         help=f'An example Arg: {name}.')


class ExampleApp(App):
    def __init__(self) -> None:
        super().__init__(help='Add a and b.')
        # Construct the Args.
        self.arg_a = ExampleArg(self, 'a')
        self.arg_b = ExampleArg(self, 'b')

    def __call__(
        self,
        args: dict[Arg] = None,
        apps: list[App] = None,
    ) -> None:
        super().__call__(args, apps)
        # Print the sum.
        a = args[self.arg_a]
        b = args[self.arg_b]
        print(f'a + b = {a} + {b} = {a + b}')


# Construct and call.
ExampleApp()()
```

The help:

```shell
./argapp.py -h
# The output:
argapp.py a b

Add a and b.

positional arguments:
  a    An example Arg: a.
  b    An example Arg: b.

optional arguments:
  -h, --help     Show the help message and exit.
```

The usage:

```shell
./argapp.py 6 -10
# The output:
a + b = 6 + -10 = -4
```
