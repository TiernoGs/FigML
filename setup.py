# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='FigML',
    version='0.1.0',
    description='Machine Learning Features In GUI',
    long_description=readme,
    author='Tierno G.',
    author_email='...',
    url='https://github.com/TiernoGs/FigML',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

