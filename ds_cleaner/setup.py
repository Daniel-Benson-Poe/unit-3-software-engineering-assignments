# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ds_cleaner",  # the name that you will install via pip
    version="1.1",
    author="Daniel Benson",
    author_email="djbenson741@gmail.com",
    description="cleans dataframes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/Daniel-Benson-Poe/unit-3-software-engineering-assignments",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)