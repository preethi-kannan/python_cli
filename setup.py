from setuptools import setup
setup(
    name = 'python_cli',
    version = '0.1.0',
    packages = ['python_cli'],
    entry_points = {
        'console_scripts': [
            'python_cli = python_cli.__main__:main'
        ]
    })