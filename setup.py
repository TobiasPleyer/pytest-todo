from setuptools import setup


setup(
    name='pytest-todo',
    version='0.1',
    author='Tobias Pleyer',
    author_email='tobi.pleyer@gmail.com',
    description='A small plugin for the pytest test framework marking '
                'TODO comments a failure',
    packages=['todo'],
    install_requires=[],
    include_package_data=True,
    entry_points = {
        'pytest11': [
            'todo = todo.plugin',
        ]
    }
)
