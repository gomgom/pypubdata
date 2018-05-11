from setuptools import setup, find_packages
import os

setup(
    name='pypubdata',
    version='0.1.4.1',
    packages=find_packages(),
    url='https://github.com/gomgomdev/pypubdata',
    download_url='https://github.com/gomgomdev/pypubdata/archive/master.zip',
    license='lGPLv3',
    author='Gomgom',
    author_email='dev@gomgom.io',
    description='It is simple module package for ROK Public Data OpenAPI.',
    long_description=open('README.rst', 'rt', encoding='utf-8').read(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5'
    ]
)