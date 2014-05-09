#! -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='naming',
      version='0.0.1',
      author='Kang Hyojun',
      author_email='hyojun@admire.kr',
      install_requires=[
          'flask==0.10.1', 'flask-script>=0.5.3', 'pytest==2.3.5',
      ],
      packages=find_packages(),
      entry_points={
          'console_scripts': ['naming = manager:run_manager']
      })
