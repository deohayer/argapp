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
        '''

    @default.setter
    def default(self, v: 'object | list | None') -> 'None':
        ...

    @property
    def choices(self) -> 'dict':
        '''
        '''

    @choices.setter
    def choices(self, v: 'dict | None') -> 'None':
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
        '''

    @suppress.setter
    def suppress(self, v: 'bool | None') -> 'None':
        ...

    @property
    def required(self) -> 'bool':
        '''
        '''

    @required.setter
    def required(self, v: 'bool | None') -> 'None':
        ...

    @property
    def append(self) -> 'bool':
        '''
        '''

    @append.setter
    def append(self, v: 'bool | None') -> 'None':
        ...

    @property
    def completer(self) -> 'Completer':
        '''
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
        '''

    @property
    def multiple(self) -> 'bool':
        '''
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
        '''

    @overload
    def __call__(
        self,
        v: 'int',
    ) -> 'int':
        '''
        '''

    @overload
    def __call__(
        self,
        v: 'str | None',
    ) -> 'object | None':
        '''
        '''

    @overload
    def __call__(
        self,
        v: 'list[str | None]',
    ) -> 'list[object | None]':
        '''
        '''

    @overload
    def __call__(
        self,
        v: 'list[str] | None',
    ) -> 'list[object] | None':
        '''
        '''

    @overload
    def __call__(
        self,
        v: 'list[list[str] | None]',
    ) -> 'list[list[object] | None]':
        '''
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
        '''

    @choices.setter
    def choices(self, v: 'bool | None') -> 'None':
        ...

    @property
    def default(self) -> 'bool':
        '''
        '''

    @default.setter
    def default(self, v: 'bool | None') -> 'None':
        ...

    def text_help(self, arg: 'Arg') -> 'str':
        '''
        '''

    def text_usage(self, arg: 'Arg') -> 'str':
        '''
        '''

    def __init__(
        self,
        choices: 'bool | None' = None,
        default: 'bool | None' = None,
    ) -> 'None':
        '''
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
