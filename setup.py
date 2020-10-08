"""
deployed versions from:

pip [dev] devpi install example
    pip install -U pip setuptools
    pip install -U -e .[dev]
"""
import codecs
import os

from setuptools import find_packages, setup

NAME = "codereddemo"
PYTHON_VER = "==3.8.*"

# Dependencies required to use your package
INSTALL_REQS = [
    "django",
    "wagtail",  # django cms
    "coderedcms",
    "django-dbbackup",
    "logzero",
    "pandas",
    "scipy",
    "seaborn",
]


# Dependencies required for development
DEV_REQS = ["jupyter", "flake8", "black", "isort", "mypy"]

# tricks for task management
# Makefile
TASK_REQS = ["doit", "fabric"]

# Dependencies required only for running tests
TEST_REQS = ["pytest", "pytest-cov"]

# Dependencies required for deploying to an index server
DEPLOYMENT_REQS = ["twine", "wheel", "m2r"]

long_description = ""
long_description_content_type = "text/markdown"


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


long_description = read("README.md")

setup(
    name=NAME,
    version="0.1.0",
    packages=find_packages(),
    install_requires=INSTALL_REQS,
    extras_require={
        "dev": TEST_REQS + DEPLOYMENT_REQS + DEV_REQS,
        "deploy": DEPLOYMENT_REQS,
        "test": TEST_REQS,
    },
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    python_requires=PYTHON_VER,
    test_suite="tests",
    tests_require=TEST_REQS,
    entry_points={"console_scripts": []},
)