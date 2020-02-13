# coding: utf-8
from setuptools import setup, find_packages
import codecs
from os import path

here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="nwpc-workflow-log-processor",

    version="2.2.0",

    description="A log processor for workflow systems in NWPC.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/nwpc-oper/nwpc-workflow-log-processor",

    author="perillaroc",
    author_email="perillaroc@gmail.com",

    license="GPLv3",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],

    keywords="nwpc workflow log processor",

    packages=find_packages(exclude=["docs", "tests", "tool"]),

    install_requires=[
        "pyyaml",
        "loguru",
        "mongoengine",
        "sqlalchemy",
        "pyspark",
        "click",
        "pymongo",
        "nwpc_workflow_model=0.5",
        "nwpc_workflow_log_model>=2,<3",
    ],

    extras_require={
        "test": ["pytest"],
        "cov": ["pytest-cov", "codecov"]
    },

    entry_points={}
)
