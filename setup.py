from setuptools import setup, find_packages

setup(
    name='north',
    version='1.0',
    packages=find_packages(),  # Automatically finds the 'pyforth' package
    py_modules=['north_cli', 'north'],  # Your CLI module
    entry_points={
        'console_scripts': [
            'north=north_cli:main',  # Command to run your script
        ],
    },
    install_requires=[],
)
