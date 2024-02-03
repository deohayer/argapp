'''
Wrapper for argparse and argcomplete.

Compatible with Python versions 3.6 - 3.11.
'''

import sys

from typing import overload


class Arg:
    '''
    '''

    @property
    def name(self) -> 'str':
        '''
        The name of the argument's value.

        Defaults:
        1. Uppercase `self.lopt`, if set.
        2. Uppercase `self.sopt`, if set.
        3. `''`.

        Exceptions:
        1. `TypeError`, if the type is not `str` or `None`.
        '''

    @name.setter
    def name(self, v: 'str | None') -> 'None':
        ...

    @property
    def lopt(self) -> 'str':
        '''
        The long option name.

        Defaults:
        1. `""`.

        Exceptions:
        1. `TypeError`, if the type is not `str` or `None`.
        '''

    @lopt.setter
    def lopt(self, v: 'str | None') -> 'None':
        ...

    @property
    def sopt(self) -> 'str':
        '''
        The short option name.

        Defaults:
        1. `""`.

        Exceptions:
        1. `TypeError`, if the type is not `str` or `None`.
        2. `ValueError`, if the value exceeds one character.
        '''

    @sopt.setter
    def sopt(self, v: 'str | None') -> 'None':
        ...

    @property
    def help(self) -> 'str':
        '''
        The argument's description.

        Defaults:
        1. `""`.

        Exceptions:
        1. `TypeError`, if the type is not `str` or `None`.
        '''

    @help.setter
    def help(self, v: 'str | None') -> 'None':
        ...

    @property
    def helper(self) -> 'ArgHelper':
        '''
        The argument's help text generator.

        Defaults:
        1. `ArgHelper()`.

        Exceptions:
        1. `TypeError` if the type is not `ArgHelper` or `None`.
        '''

    @helper.setter
    def helper(self, v: 'ArgHelper | None') -> 'None':
        ...

    @property
    def type(self) -> 'type':
        '''
        The type of an individual value.

        Defaults:
        . Always `bool`, if `self.flag` is `True`.
        . The type of the first item of `self.default`, if its type is `list` and it is not empty.
        . The type of `self.default`, if its type is not `list` and it is not `None`.
        . `str`.

        Exceptions:
        . `TypeError`, if the type is not `type` or `None`.
        . `ValueError`, if the value does not match `self.default`.
        '''

    @type.setter
    def type(self, v: 'type | None') -> 'None':
        ...

    @property
    def count(self) -> 'int | str':
        '''
        The number of values consumed by the argument:
        1. `0`: indicates a flag. Can be set if `self.optional` is `True`.
        2. `1`: a single value.
        3. `2` or greater: multiple values, an exact number.
        4. `'?'`: a single value, zero or one.
        5. `'*'`: multiple values, zero or more.
        6. `'+'`: multiple values, one or more.
        7. `'~'`: multiple values, zero or more. Consume the rest of the command line without parsing. Can be set if `self.positional` is `True`.

        Defaults:
        1. `'*'`, if the type of `self.default` is `list`.
        2. `1`.

        Exceptions:
        1. `TypeError`, if the type is not `int`, `str` or `None`.
        2. `ValueError`, if the type is `int` and the value is negative.
        3. `ValueError`, if the type is `str` and the value is not one of: `'?'`, `'*'`, `'+'`, `'~'`.
        4. `ValueError`, if the value is `0` and `self.optional` is `False`.
        5. `ValueError`, if the value is `'~'` and `self.positional` is `False`.
        6. `ValueError`, if the value is `'+'` and `self.default` is an empty `list`.
        7. `ValueError`, if the type is `int` and the value does not match the number of items in `self.default`.
        '''

    @count.setter
    def count(self, v: 'int | str | None') -> 'None':
        ...

    @property
    def default(self) -> 'object | list | None':
        '''
        The default value. It is used by the base implementations of `Arg.__call__(...)` in the following cases:
         * `self.count` is `'?'`, `'*'` or `'~'` and no values provided.
         * `self.optional` is `True`, `self.suppress` is `False`, and the argument is not mentioned.

        Defaults:
        1. `False`, if `self.flag` is `True`.
        2. `[]`, if `self.count` is `'*'` or `'~'`.
        3. `None`.

        Exceptions:
        1 `TypeError`, if the type is not `list` or `None` and `self.multiple` is `True`.
        2 `TypeError`, if the type is `list`, and `self.single` is `True`.
        3 `TypeError`, if the type is not `list` and it is not `self.type` or `None`.
        4 `TypeError`, if the type is `list` and one of the items is not `self.type`.
        5. `ValueError`, if the type is `list`, and the number of items does not match `self.count`.
        6. `ValueError`, if the value is an empty `list`, and `self.count` is `'+'`.
        '''

    @default.setter
    def default(self, v: 'object | list | None') -> 'None':
        ...

    @property
    def choices(self) -> 'dict[str, str]':
        '''
        A `dict` of the possible values.
         * Converted to a `dict[str, str]` from any `Iterable`.
         * The dictionary values are used as the descriptions, if not empty.
         * `self.default` is never checked against `self.choices`.

        Defaults:
        1. `{}`.

        Exceptions:
        1. `TypeError`, if the type is not `Iterable` or `None`.
        '''

    @choices.setter
    def choices(self, v: 'list | dict | None') -> 'None':
        ...

    @property
    def restrict(self) -> 'bool':
        '''
        Whether `self.choices` are restrictive.

        Defaults:
        1. `True`.

        Exceptions:
        1. `TypeError`, if the type is not `bool` or `None`.
        '''

    @restrict.setter
    def restrict(self, v: 'bool | None') -> 'None':
        ...

    @property
    def suppress(self) -> 'bool':
        '''
        Whether to not set the optional argument to `self.default` if it is not mentioned.

        Defaults:
        1. Always `False`, if `self.optional` is `False`.
        2. `False`.

        Exceptions:
        1. `TypeError`, if the type is not `bool` or `None`.
        '''

    @suppress.setter
    def suppress(self, v: 'bool | None') -> 'None':
        ...

    @property
    def required(self) -> 'bool':
        '''
        Whether the optional argument must be mentioned.

        Defaults:
        1. Always `True`, if `self.optional` is `False`.
        2. `False`.

        Exceptions:
        1. `TypeError`, if the type is not `bool` or `None`.
        '''

    @required.setter
    def required(self, v: 'bool | None') -> 'None':
        ...

    @property
    def append(self) -> 'bool':
        '''
        Whether the optional argument is appended on repeat.

        Defaults:
        1. Always `False`, if `self.optional` is `False`.
        2. `False`.

        Exceptions:
        . `TypeError`, if the type is not `bool` or `None`.
        '''

    @append.setter
    def append(self, v: 'bool | None') -> 'None':
        ...

    @property
    def completer(self) -> 'Completer':
        '''
        The command line completer for the argument.

        Defaults:
        1. `CompleterList(self.choices)`, if `self.choices` is not empty.
        2. `CompleterPath()`, if `self.type` is `str`.
        3. `CompleterNone()`.

        Exceptions:
        1. `TypeError`, if the type is not `Completer` or `None`.
        '''

    @completer.setter
    def completer(self, v: 'Completer | None') -> 'None':
        ...

    @property
    def optional(self) -> 'bool':
        '''
        Whether the argument is optional.

        Defaults:
        1. `True`, if either `self.sopt` or `self.lopt` is set.
        2. `False`.
        '''

    @property
    def positional(self) -> 'bool':
        '''
        Whether the argument is positional.

        Defaults:
        1. `True`, if both `self.sopt` and `self.lopt` are not set.
        2. `False`.
        '''

    @property
    def flag(self) -> 'bool':
        '''
        Whether the argument does not consume a value.

        Defaults:
        1. `True`, if `self.count` is `0`.
        2. `False`.
        '''

    @property
    def single(self) -> 'bool':
        '''
        Whether the argument can consume at most one value.

        Defaults:
        1. `True`, if `self.count` is `'?'` or `1`.
        2. `False`.
        '''

    @property
    def multiple(self) -> 'bool':
        '''
        Whether the argument can consume more than one value.

        Defaults:
        1. `True`, if `self.count` is `'*'`, `'+'`, `'~'` or greater than one.
        2. `False`.
        '''

    def __init__(
        self,
        name: 'str | None' = None,
        lopt: 'str | None' = None,
        sopt: 'str | None' = None,
        help: 'str | None' = None,
        helper: 'ArgHelper | None' = None,
        type: 'type | None' = None,
        count: 'int | str | None' = None,
        default: 'object | list | None' = None,
        choices: 'dict | None' = None,
        restrict: 'bool | None' = None,
        suppress: 'bool | None' = None,
        required: 'bool | None' = None,
        append: 'bool | None' = None,
        completer: 'Completer | None' = None,
    ) -> 'None':
        '''
        The constructor. Sets each field in the declaration order.

        Parameters:
        * `name` - corresponds to `self.name`.
        * `lopt` - corresponds to `self.lopt`.
        * `sopt` - corresponds to `self.sopt`.
        * `help` - corresponds to `self.help`.
        * `helper` - corresponds to `self.helper`.
        * `type` - corresponds to `self.type`.
        * `count` - corresponds to `self.count`.
        * `default` - corresponds to `self.default`.
        * `choices` - corresponds to `self.choices`.
        * `restrict` - corresponds to `self.restrict`.
        * `suppress` - corresponds to `self.suppress`.
        * `required` - corresponds to `self.required`.
        * `append` - corresponds to `self.append`.
        * `completer` - corresponds to `self.completer`.
        '''

    @overload
    def __call__(
        self,
        v: 'bool',
    ) -> 'bool':
        '''
        Parse the command line value. This overload is called if:
         * `self.flag` is `True`.
         * `self.append` is `False`.

        Parameters:
         * `v` - `True` if the argument is mentioned in the command line. `False` otherwise.

        Returns:
        1. `self.default`, if v is `True`.
        2. `not self.default`, if v is `False`.
        '''

    @overload
    def __call__(
        self,
        v: 'int',
    ) -> 'int':
        '''
        Parse the command line value. This overload is called if:
         * `self.flag` is `True`.
         * `self.append` is `True`.

        Parameters:
         * `v` - a number of times the argument is mentioned in the command line.

        Returns:
        1. `v`.
        '''

    @overload
    def __call__(
        self,
        v: 'str | None',
    ) -> 'object | None':
        '''
        Parse the command line value. This overload is called if:
         * `self.single` is `True`.
         * `self.append` is `False`.

        Parameters:
         * `v` - a value from the command line. `None` if not provided.

        Returns:
        1. `self.default`, if `v` is `None`.
        2. `self.type(v)`.

        Exceptions:
        1. `CallError`, if `self.restrict` is `True` and the value is not in `self.choices`.
        '''

    @overload
    def __call__(
        self,
        v: 'list[str | None]',
    ) -> 'list[object | None]':
        '''
        Parse the command line value. This overload is called if:
         * `self.single` is `True`.
         * `self.append` is `True`.

        Parameters:
         * `v` - a list of values from the command line associated with the argument.

        Returns:
        1. A `list` where each item `x` from `v` is set to:
            1. `self.default`, if `x` is `None`.
            2. `self.type(x)`.

        Exceptions:
        . `CallError`, if `self.restrict` is `True` and any item is not in `self.choices`.
        '''

    @overload
    def __call__(
        self,
        v: 'list[str] | None',
    ) -> 'list[object] | None':
        '''
        Parse the command line value. This overload is called if:
         * `self.multiple` is `True`.
         * `self.append` is `False`.

        Parameters:
         * `v` - a list of values from the command line.

        Returns:
        1. `self.default`, if `v` is `None`.
        2. A `list` where each item `x` from `v` is set to `self.type(x)`.

        Exceptions:
        1. `CallError`, if `self.restrict` is `True` and any item is not in `self.choices`.
        '''

    @overload
    def __call__(
        self,
        v: 'list[list[str] | None]',
    ) -> 'list[list[object] | None]':
        '''
        Parse the command line value. This overload is called if:
         * `self.multiple` is `True`.
         * `self.append` is `True`.

        Parameters:
         * `v` - a list of lists of values from the command line associated with the argument.

        Returns:
        1. A `list[list]` where each list `l` from `v` is converted to:
            1. `self.default`, if `l` is `None`.
            2. A `list` where each item `x` from `l` is converted to `self.type(x)`.

        Exceptions:
        1. `CallError`, if `self.restrict` is `True` and any item is not in `self.choices`.
        '''


class App:
    '''
    '''

    @property
    def name(self) -> 'str':
        '''
        '''

    @name.setter
    def name(self, v: 'str | None') -> 'None':
        ...

    @property
    def help(self) -> 'str':
        '''
        '''

    @help.setter
    def help(self, v: 'str | None') -> 'None':
        ...

    @property
    def prolog(self) -> 'str':
        '''
        '''

    @prolog.setter
    def prolog(self, v: 'str | None') -> 'None':
        ...

    @property
    def epilog(self) -> 'str':
        '''
        '''

    @epilog.setter
    def epilog(self, v: 'str | None') -> 'None':
        ...

    @property
    def helper(self) -> 'AppHelper':
        '''
        '''

    @helper.setter
    def helper(self, v: 'AppHelper | None') -> 'None':
        ...

    @property
    def args(self) -> 'list[Arg]':
        '''
        '''

    @property
    def apps(self) -> 'list[App]':
        '''
        '''

    def __init__(
        self,
        name: 'str | None' = None,
        help: 'str | None' = None,
        epilog: 'str | None' = None,
        prolog: 'str | None' = None,
        helper: 'AppHelper | None' = None,
    ) -> 'None':
        '''
        '''

    def __call__(
        self,
        args: 'dict[Arg]',
        apps: 'list[App]',
    ) -> 'None':
        '''
        '''


class ArgHelper:
    '''
    '''

    @property
    def choices(self) -> 'bool':
        '''
        Whether to append the `Arg.choices` to the help text.

        Defaults:
        1. `True`.

        Exceptions:
        1. `TypeError`, if the type is not `bool` or `None`.
        '''

    @choices.setter
    def choices(self, v: 'bool | None') -> 'None':
        ...

    @property
    def default(self) -> 'bool':
        '''
        Whether to append the `Arg.default` to the help text.

        Defaults:
        1. `True`.

        Exceptions:
        1. `TypeError`, if the type is not `bool` or `None`.
        '''

    @default.setter
    def default(self, v: 'bool | None') -> 'None':
        ...

    def text_help(self, arg: 'Arg') -> 'str':
        '''
        Generate the argument's description.

        Parameters:
         * `arg` - the argument to use for the generation.

        Returns:
        1. `arg.help` with the following appended if `arg.flag` is `False`:
           * `arg.default`, if `self.default` is `True`.
           * `arg.choices`, if `self.choices` is `True`.
        '''

    def text_usage(self, arg: 'Arg') -> 'str':
        '''
        Generate the argument's usage (stylized name).

        Parameters:
        * `arg` - the argument to use for the generation.

        Returns:
        1. A `str` with the following text combined:
           1. `-sopt`, if `arg.sopt` is set.
           2. `--lopt`, if `arg.lopt` is set.
           3. A stylized `arg.name`:
              1. `name` repeated `arg.count` times, if its type is `int`.
              2. `[name]`, if `arg.count` is `'?'`.
              3. `[name...]`, if `arg.count` is `'*'`.
              4. `name [name...]`, if `arg.count` is `'+'`.
              5. `[name]...`, if `arg.count` is `'~'`.
        '''

    def __init__(
        self,
        choices: 'bool | None' = None,
        default: 'bool | None' = None,
    ) -> 'None':
        '''
        The constructor. Sets each field in the declaration order.

        Parameters:
         * `choices` - corresponds to `self.choices`.
         * `default` - corresponds to `self.default`.
        '''


class AppHelper:
    '''
    '''

    @property
    def lopt(self) -> 'str':
        '''
        '''

    @lopt.setter
    def lopt(self, v: 'str | None') -> 'None':
        ...

    @property
    def sopt(self) -> 'str':
        '''
        '''

    @sopt.setter
    def sopt(self, v: 'str | None') -> 'None':
        ...

    @property
    def help(self) -> 'str':
        '''
        '''

    @help.setter
    def help(self, v: 'str | None') -> 'None':
        ...

    def text_help(
        self,
        apps: 'list[App]',
        name: 'str',
    ) -> 'str':
        '''
        '''

    def text_usage(
        self,
        apps: 'list[App]',
        name: 'str',
    ) -> 'str':
        '''
        '''

    def section_prolog(
        self,
        title: 'str',
        app: 'App',
    ) -> 'str':
        '''
        '''

    def section_epilog(
        self,
        title: 'str',
        app: 'App',
    ) -> 'str':
        '''
        '''

    def section_apps(
        self,
        title: 'str',
        apps: 'list[App]',
    ) -> 'str':
        '''
        '''

    def section_args(
        self,
        title: 'str',
        apps: 'list[Arg]',
    ) -> 'str':
        '''
        '''

    def __init__(
        self,
        lopt: 'str | None' = 'help',
        sopt: 'str | None' = 'h',
        help: 'str | None' = 'Show the help text and exit.',
    ) -> 'None':
        '''
        '''


class Completer:
    '''
    '''


class CompleterNone:
    '''
    '''


class CompleterList:
    '''
    '''


class CompleterPath:
    '''
    '''


class CallError:
    '''
    '''

    @property
    def text(self) -> 'str':
        '''
        '''

    @text.setter
    def text(self, v: 'str | None') -> 'None':
        ...

    @property
    def code(self) -> 'int':
        '''
        '''

    @code.setter
    def code(self, v: 'int | None') -> 'None':
        ...

    def __init__(
        self,
        text: 'str | None' = None,
        code: 'int | None' = None,
    ) -> 'None':
        '''
        '''


def main(
    app: 'App',
    argv: 'list[str]' = sys.argv,
) -> 'None':
    '''
    '''


def _str(o: 'object') -> 'str':
    '''
    Convert to a printable `str`.

    Parameters:
     * `o` - object to convert to `str`.

    Returns:
    1. `f'"{o}"'`, if the type is `str`.
    2. `o__name__`, if the type is `type`.
    3. `str(o)`.
    '''


def _raise_t(
    o: 'object',
    t: 'type | tuple[type]',
    v: 'str',
) -> 'None':
    '''
    Raise a consistently formatted `TypeError`, if the object is not one of the types.

    Parameters:
     * `o` - object to check.
     * `t` - types to check against.
     * `v` - name of the value that is being checked.

    Exceptions:
     * `TypeError`, if the type of `o` does not match any in `t`.
    '''


def _raise_v(
    o: 'object',
    c: 'bool',
    v: 'str',
    m: 'str',
) -> 'None':
    '''
    Raise a consistently formatted `ValueError`, if the condition is `False`.

    Parameters:
     * `o` - object, will be mentioned in the error message.
     * `c` - condition, `True` or `False`.
     * `v` - name of the value that is being checked.
     * `m` - message with more datails.

    Exceptions:
     * `ValueError`, if `c` is `False`.
    '''
