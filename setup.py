from setuptools import setup, find_packages

setup(
    name='pyforth',
    version='1.0',
    packages=find_packages(),  # Automatically finds the 'pyforth' package
    py_modules=['pyforth_cli', 'pyforth'],  # Your CLI module
    entry_points={
        'console_scripts': [
            'pyforth=pyforth_cli:main',  # Command to run your script
        ],
    },
    install_requires=[],
)
