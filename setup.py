from setuptools import setup
import io
import os


def read(file_name):
    """Read a text file and return the content as a string."""
    with io.open(os.path.join(os.path.dirname(__file__), file_name),
                 encoding='utf-8') as f:
        return f.read()


setup(
    name='pytest-todo',
    version='0.2.1',
    author='Tobias Pleyer',
    author_email='tobi.pleyer@gmail.com',
    description='A small plugin for the pytest testing framework, marking '
                'TODO comments as failure',
    long_description=read('README.rst'),
    packages=['todo'],
    install_requires=['pytest'],
    long_description_content_type='text/x-rst',
    include_package_data=True,
    url='https://github.com/TobiasPleyer/pytest-todo',
    license='MIT',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
    ],
    entry_points = {
        'pytest11': [
            'todo = todo.plugin',
        ]
    }
)
