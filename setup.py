from setuptools import setup, find_packages
from Cython.Build import cythonize
import numpy as np

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = find_packages()

setup(
    name="Kivy Games",
    version="0.0.1",
    author="Jonathan J Watson",
    description="A collection of simple games made with Kivy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonathanjameswatson/kivy-games",
    license="MIT",
    python_requires="~=3.6",
    packages=packages,
    ext_modules=cythonize("kivygames/games/noughtsandcrosses/c.pyx"),
    include_dirs=[np.get_include()],
)
