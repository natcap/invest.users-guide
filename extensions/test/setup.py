from setuptools import setup
import os

print('setup.py', os.getcwd())


setup(name='natcap.invest',
      version='0.1',
      packages=['test_module'],
      zip_safe=False)
