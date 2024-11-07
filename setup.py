from setuptools import setup, find_packages

setup(
    name="MySQL-DataBridge",
    version="0.1.2",
    author="H-Rasheed",
    author_email="rsm878yourkhan@gmail.com",
     description="A lightweight Python module to simplify MySQL database connections and queries.",
    long_description="MySQL-DataBridge is a Python package designed to streamline MySQL database interactions, allowing easy connection management and query handling.",
    long_description_content_type="text/markdown",
    url="https://github.com/Manti-Rashee/MySQL-DataBridge",  # Link to the project repo
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "mysql-connector-python"
    ],
)
