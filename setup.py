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
