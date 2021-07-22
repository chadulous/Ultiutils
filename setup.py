import pathlib
from setuptools import setup
import os
import requests
import random
os.system('rm dist/* && rmdir build/* && rmdir build/')
# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ultiutils",
    version='1.0.2',
    description="utilites module to make coding in python just wayyy faster",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/maverick-dev-55/Ultiutils",
    author="toxikdevswastaken",
    author_email="pypi@toxik.cf",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["ultiutils"],
    include_package_data=True,
    install_requires=["requests"],
)
os.system('twine check dist/* > check.txt')
check = open('check.txt', 'r').read()
if check.count('PASSED') == 2:
  os.system('twine upload --disable-progress-bar  --skip-existing --non-interactive dist/*')