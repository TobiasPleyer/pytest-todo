from setuptools import setup


setup(
    name='pytest-todo',
    version='0.2',
    author='Tobias Pleyer',
    author_email='tobi.pleyer@gmail.com',
    description='A small plugin for the pytest testing framework, marking '
                'TODO comments as failure',
    packages=['todo'],
    install_requires=['pytest'],
    include_package_data=True,
    entry_points = {
        'pytest11': [
            'todo = todo.plugin',
        ]
    }
)
