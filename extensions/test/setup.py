from setuptools import setup
import os

print('setup.py', os.getcwd())


setup(
    name='natcap.invest',
    version='0.1',
    packages=['natcap.invest'],
    package_dir={
        'natcap.invest': 'test_module'
    },
    zip_safe=False)
