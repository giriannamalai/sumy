# -*- coding: utf8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sumy


with open("README.rst") as readme:
    with open("CHANGELOG.rst") as changelog:
        long_description = readme.read() + "\n\n" + changelog.read()

with open("LICENSE.rst") as file:
    license = file.read()


setup(
    name="sumy",
    version=sumy.__version__,
    description="Module for automatic text summarization of HTML documents.",
    long_description=long_description,
    author="Michal Belica",
    author_email="miso.belica@gmail.com",
    url="https://github.com/miso-belica/sumy",
    license=license,
    keywords=[
        "data mining",
        "text summarization",
        "data reduction",
        "web-data extraction",
        "NLP",
        "natural language processing",
        "latent semantic analysis",
        "LSA",
        "singular value decomposition",
        "SVD"
    ],
    dependency_links = [
        "http://github.com/miso-belica/readability.py/tarball/master",
    ],
    install_requires=[
        "docopt>=0.6.1,<0.7",
        "nltk",
    ],
    tests_require=[
        "nose",
        "coverage",
    ],
    test_suite="nose.collector",
    extras_require={
        "LSA": ["numpy", "scipy"],
    },
    packages=[
        "sumy",
        "sumy.evaluation",
        "sumy.models",
        "sumy.models.dom",
        "sumy.parsers",
        "sumy.nlp",
        "sumy.nlp.stemmers",
        "sumy.summarizers",
    ],
    package_data={"sumy": [
        "data/stopwords/*.txt",
        "data/tokenizers/*.pickle",
    ]},
    entry_points={
        "console_scripts": [
            "sumy=sumy.__main__:main",
        ]
    },
    classifiers=(
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Natural Language :: Czech",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Education",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing :: Markup :: HTML",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        # "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.3",
    ),
)
