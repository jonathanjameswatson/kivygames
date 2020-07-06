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
    url="https://github.com/jonathanjameswatson/kivygames",
    license="MIT",
    install_requires=[
        "wheel",
        "setuptools",
        "importlib_resources ;python_version<'3.7'",
        "pygame",
        "cython>=0.24,<=0.29.14,!=0.27,!=0.27.2",
        "kivy_deps.glew;platform_system=='Windows'",
        "kivy_deps.sdl2;platform_system=='Windows'",
        "kivy_deps.gstreamer;platform_system=='Windows'",
        "kivy>=2.0.0rc2",
        "screeninfo;platform_system!='Darwin'",
        "numpy",
    ],
    python_requires="~=3.6",
    entry_points={"console_scripts": ["kivygames=kivygames.__main__:run"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    packages=packages,
    ext_modules=cythonize("kivygames/games/noughtsandcrosses/c.pyx"),
    include_dirs=[np.get_include()],
)
