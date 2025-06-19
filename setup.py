from setuptools import setup, find_packages

setup(
    name="lib_calculadora",
    version="1.0",
    packages=find_packages(),
    description="Uma biblioteca de operações matemáticas com FastAPI exceptions.",
    author="Nathan Goncalves",
    author_email="nathanwow12@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "fastapi"
    ]
)