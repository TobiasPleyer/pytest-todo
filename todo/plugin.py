import pytest
from os.path import relpath


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption(
        '--todo', action='store_true',
        help="Check for TODO comments in .py files")


def pytest_collect_file(path, parent):
    config = parent.config
    if config.option.todo and path.ext == '.py':
        return TodoItem(path, parent)


class TodoError(Exception):
    """The custom error class for TODO checks"""


class TodoItem(pytest.Item, pytest.File):

    def runtest(self):
        checker = check_todo(self.fspath)
        if checker.hasErrors:
            raise TodoError(checker.summary())

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(TodoError):
            return excinfo.value.args[0]
        return super(TodoItem, self).repr_failure(excinfo)


def check_todo(path):
    options = {}
    from todo.checker import TodoChecker
    checker = TodoChecker(options, relpath(path))
    checker.check()
    return checker
