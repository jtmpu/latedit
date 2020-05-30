# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from os import listdir
from os.path import expanduser, join, isfile
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

binaries = listdir("bin")
binaries = map(lambda x: join("bin", x), binaries)
binaries = filter(isfile, binaries)
# Only automatically adds binaries with .py extension
binaries = filter(lambda x: x.endswith(".py"), binaries)
binaries = list(binaries)

home = expanduser("~")
envfolder = join(home, ".latedit")
# Assumes setup is run from the current directory, as everythig else
templates = listdir("resources/templates")
templates = map(lambda x: join("resources/templates", x), templates)
templates = filter(isfile, templates)
templates = list(templates)
examples = listdir("resources/example-document")
examples = map(lambda x: join("resources/example-document", x), examples)
examples = filter(isfile, examples)
examples = filter(lambda x: x.endswith(".tex"), examples)
examples = list(examples)
configfiles = [
    (join(envfolder, "templates"), templates),
    (join(envfolder, "example"), examples)
]

setup(
    name='latedit',
    version='0.0.1',
    description='Edit, or use templates for latex documents via CLI tools or python APIs',
    long_description=readme,
    author='Joakim Valberg',
    author_email='',
    url='https://github.com/jtmpu/latedit',
    license=license,
    install_requires=requirements,
    scripts=binaries,
    data_files=configfiles,
    packages=find_packages(exclude=('tests', 'docs'))
)
