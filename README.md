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

### `Arg.app`

The application that contains the argument. The `Arg` is added to `app.args`.

Must be set via `Arg.__init__` as `app`:
 * `type(app)` must be `App` (`TypeError`).
 * `app.args` must not contain `Arg` with:
   1. The same `Arg.lopt` or `Arg.sopt` if `Arg.is_optional` is `True` (`ValueError`).
   2. The same `Arg.name` if `Arg.is_positional` is `True` (`ValueError`).

#### Declaration

```python
@property
def app(self) -> App:
    ...
```

#### Example

```python
class ExampleApp(App):
    def __init__(self) -> None:
        super().__init__(name='argapp.py')
        # OK:
        #  * name of positional Args are different.
        #  * sopt and lopt of optional Args are different.
        #  * name of optional Args are not considered.
        #  * sopt, lopt, name of the same object do not clash.
        #  * Optional and positional Args cannot clash.
        self.arg_p1 = Arg(app=self,
                          name='a')
        self.arg_p2 = Arg(app=self,
                          name='b')
        self.arg_o1 = Arg(app=self,
                          name='a',
                          sopt='a',
                          lopt='a')
        self.arg_o2 = Arg(app=self,
                          name='b',
                          sopt='b',
                          lopt='b')
        self.arg_o3 = Arg(app=self,
                          name='a',
                          sopt='c',
                          lopt='c')
        # TypeError: Invalid type of Arg.app: None. Expected: App.
        self.arg2 = Arg(app=None)
        # TypeError: Invalid type of Arg.app: bool. Expected: App.
        self.arg2 = Arg(app=False)
        # ValueError: Invalid value of Arg.name: "a". Must not repeat other Arg.name in argapp.py App.
        self.arg1 = Arg(app=self,
                        name='a')
        self.arg2 = Arg(app=self,
                        name='a')
        # ValueError: Invalid value of Arg.sopt: "a". Must not repeat other Arg.sopt in argapp.py App.
        self.arg1 = Arg(app=self,
                        sopt='a')
        self.arg2 = Arg(app=self,
                        sopt='a')
        # ValueError: Invalid value of Arg.lopt: "a". Must not repeat other Arg.lopt in argapp.py App.
        self.arg1 = Arg(app=self,
                        lopt='a')
        self.arg2 = Arg(app=self,
                        lopt='a')
```

### `Arg.name`

The value name: `"URI"` in `"-u URI, --uri URI"`.

May be set via `Arg.__init__` as `name`:
 * `type(name)` must be `str` or `None` (`TypeError`).
 * `len(name)` must be greater than 0 (`ValueError`).

Defaults:
1. `Arg.lopt.upper()`, if `Arg.lopt` is not `None`.
2. `Arg.sopt.upper()`, if `Arg.sopt` is not `None`.
3. `"ARG"`, if none of the above applies.

#### Declaration

```python
@property
def name(self) -> str:
    ...
```

#### Example

```python
class ExampleApp(App):
    def __init__(self) -> None:
        super().__init__(name='argapp.py')
        # OK, the trivial case.
        self.arg = Arg(app=self,
                       name='arg')
        # OK, the name defaults to "ARG".
        self.arg = Arg(app=self)
        # OK, the name defaults to "O".
        self.arg = Arg(app=self,
                       sopt='o')
        # OK, the name defaults to "OPT".
        self.arg = Arg(app=self,
                       lopt='opt')
        # OK, the name defaults to "OPT" (lopt prioritized).
        self.arg = Arg(app=self,
                       sopt='o',
                       lopt='opt')
        # TypeError: Invalid type of Arg.name: bool. Expected: str, None.
        self.arg = Arg(app=self,
                       name=False)
        # ValueError: Invalid value of Arg.name: "". Must not be empty.
        self.arg = Arg(app=self,
                       name='')
```

### `Arg.sopt`

The short option name: `"-u"` in `"-u URI, --uri URI"`.
 * The leading `"-"` must be ommited.
 * Makes the `Arg` optional.

May be set via `Arg.__init__` as `sopt`:
 * `type(sopt)` must be `str` or `None` (`TypeError`).
 * `len(sopt)` must be 1 (`ValueError`).

#### Declaration

```python
@property
def sopt(self) -> str | None:
    ...
```

#### Example

```python
class ExampleApp(App):
    def __init__(self) -> None:
        super().__init__(name='argapp.py')
        # OK, the trivial case.
        self.arg = Arg(app=self,
                       sopt='a')
        # OK, sopt is None and the Arg is not optional.
        self.arg = Arg(app=self,
                       sopt=None)
        # TypeError: Invalid type of Arg.sopt: bool. Expected: str, None.
        self.arg = Arg(app=self,
                       sopt=False)
        # ValueError: Invalid value of Arg.sopt: "". Must be a single character.
        self.arg = Arg(app=self,
                       sopt='')
        # ValueError: Invalid value of Arg.sopt: "arg". Must be a single character.
        self.arg = Arg(app=self,
                       sopt='arg')
```

### `Arg.lopt`

The long option name: `"--uri"` in `"-u URI, --uri URI"`.
 * The leading `"--"` must be ommited.
 * Makes the `Arg` optional.

May be set via `Arg.__init__` as `lopt`:
 * `type(lopt)` must be `str` or `None` (`TypeError`).
 * `len(lopt)` must be greater than 0 (`ValueError`).

#### Declaration

```python
@property
def lopt(self) -> str | None:
    ...
```

#### Example

```python
class ExampleApp(App):
    def __init__(self) -> None:
        super().__init__(name='argapp.py')
        # OK, the trivial case.
        self.arg = Arg(app=self,
                       lopt='arg')
        # OK, lopt is None and the Arg is not optional.
        self.arg = Arg(app=self,
                       lopt=None)
        # TypeError: Invalid type of Arg.lopt: bool. Expected: str, None.
        self.arg = Arg(app=self,
                       lopt=False)
        # ValueError: Invalid value of Arg.lopt: "". Must be a non-empty str.
        self.arg = Arg(app=self,
                       lopt='')
```

### `Arg.help`

The help text.

May be set via `Arg.__init__` as `help`:
 * `type(help)` must be `str` or `None` (`TypeError`).

If `Arg.choices` is not `None`, the items are appended to the help text.
`help1` and `help2` are only added if `type(Arg.choices) == dict`:

```text
Possible values:
 * value1 - help1
 * value2 - help2
 * (...)
 ```

If `Arg.default` is not `None`, the following text is appended:

```text
Defaults to: value1 (value2, ...).
```

Defaults:
1. `""`.

#### Declaration

```python
@property
def help(self) -> str:
    ...
```

#### Example

```python
class ExampleApp(App):
    def __init__(self) -> None:
        super().__init__(name='argapp.py')
        # OK, the trivial case:
        #   ARG    A help text.
        self.arg = Arg(app=self,
                       help='A help text.')
        # OK, the newlines are retained and properly padded:
        #   ARG    This is a:
        #          1. Multiline.
        #          2. Help.
        #          3. Text.
        self.arg = Arg(app=self,
                       help=str(
                           'This is a:\n'
                           '1. Multiline.\n'
                           '2. Help.\n'
                           '3. Text.'))
        # OK, help defaults to "":
        #   ARG
        self.arg = Arg(app=self)
        # OK, choices list is appended:
        #   ARG    Possible values:
        #           * value1
        #           * value2
        self.arg = Arg(app=self,
                       choices=['value1', 'value2'])
        # OK, choices dict is appended:
        #   ARG    An Arg with choices.
        #          Possible values:
        #           * value1
        #           * value2 - help2
        self.arg = Arg(app=self,
                       help='An Arg with choices.',
                       choices={'value1': '', 'value2': 'help2'})
        # OK, default is appended:
        #   ARG    Defaults to: arg
        self.arg = Arg(app=self,
                       default='arg')
        # OK, default list is appended:
        #   ARG    An Arg with default.
        #          Defaults to: value1 value2
        self.arg = Arg(app=self,
                       count='*',
                       help='An Arg with default.',
                       default=['value1', 'value2'])
        # OK, both are appended:
        #   ARG    An Arg with both.
        #          Possible values:
        #           * value1
        #           * value2 - help2
        #          Defaults to: value1 value2
        self.arg = Arg(app=self,
                       count='*',
                       help='An Arg with both.',
                       choices={'value1': '', 'value2': 'help2'},
                       default=['value1', 'value2'])
        # TypeError: Invalid type of Arg.help: bool. Expected: str, None.
        self.arg = Arg(app=self,
                       help=False)
```
