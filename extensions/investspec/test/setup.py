from setuptools import setup
import os

print('setup.py', os.getcwd())


setup(
    name='test_module',
    version='0.1',
    packages=['test_module'],
    zip_safe=False)
