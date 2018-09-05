# coding=utf-8
import os

from setuptools import setup, find_packages


def read(fname):
    """
    Utility function to read the README file. Used for the long_description.
    :param fname:
    :return:
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="bpmn_python",
    version="0.0.19-SNAPSHOT",
    author="Izbela Smietana, Krzysztof Honkisz",
    # author_email = "honkiszkrzystof@gmail.com",
    description=("Python library that allows to import/export BPMN diagram (as an XML file) and provides a simple "
                 "visualization capabilities."),
    license="GNU GENERAL PUBLIC LICENSE",
    keywords=["bpmn", "xml"],
    url="https://github.com/KrzyHonk/bpmn-python",
    download_url="https://github.com/KrzyHonk/bpmn-python/tarball/0.0.19-SNAPSHOT",
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
'wiktionaryparser==0.0.5',
'networkx==1.11',
'nltk==3.2.5',
'numpy==1.13.3',
'pip==9.0.1',
'JCC==3.0',
'six==1.11.0',
'pydotplus==2.0.2',
'pandas==0.21.0',
'matplotlib==2.0.0'
    ],
    long_description=read('README.md'),
)
