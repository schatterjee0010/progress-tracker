from setuptools import setup, find_packages

with open("README.md", "r") as fl:
    long_desc = fl.read()

setup(
    name="generic_libs",
    version="0.0.1",
    author="S Chatterjee",
    description="Generic Libraries",
    long_description=long_desc,
    url="https://github.com/schatterjee01/progress-tracker",
    package_dir={'': 'src'},
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "test"]),
    install_requires=['xmltodict'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["generic_libs"],
)