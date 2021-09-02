from setuptools import setup, find_packages

with open("README.md", "r") as fl:
    long_desc = fl.read()

setup(
    name="generic_libs",
    version="0.0.2",
    author="S Chatterjee",
    author_email="schatterjee0010@gmail.com",
    description="Generic Libraries",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    project_urls={
        "Source": "https://github.com/schatterjeecs/generic-libs",
        "Documentation": "https://github.com/schatterjeecs/generic-libs#readme",
    },
    url="https://github.com/schatterjeecs/generic-libs",
    package_dir={'': 'src'},
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "test"]),
    install_requires=['xmltodict'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
