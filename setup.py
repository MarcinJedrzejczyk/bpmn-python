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
		'JCC==3.0',
'attrs==17.3.0',
'backports.functools-lru-cache==1.4',
'beautifulsoup4==4.6.0',
'bpmn-python==0.0.18',
'certifi==2018.4.16',
'chardet==3.0.4',
'colorama==0.3.9',
'cycler==0.10.0',
'decorator==4.1.2',
'funcsigs==1.0.2',
'functools32==3.2.3.post2',
'idna==2.6',
'isodate==0.6.0',
'lupyne==2.0',
'matplotlib==2.0.0',
'networkx==1.11',
'nltk==3.2.5',
'numpy==1.13.3',
'pandas==0.21.0',
'pip==9.0.1',
'pluggy==0.6.0',
'py==1.5.2',
'pydotplus==2.0.2',
'pyparsing==2.2.0',
'pytest==3.3.1',
'python-dateutil==2.6.1',
'pytz==2017.3',
'rdf==0.9a6',
'rdflib==4.2.2',
'requests==2.18.4',
'setuptools==28.8.0',
'six==1.11.0',
'urllib3==1.22',
'wiktionaryparser==0.0.5'
    ],
    long_description=read('README.md'),
)
