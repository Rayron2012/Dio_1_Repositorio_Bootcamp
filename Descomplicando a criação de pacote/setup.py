from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="Rayron Soares",
    author_email="rayron2013@gmail.com",
    description="Meu primeiro pacote de teste",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rayron2012/Dio_1_Repositorio_Bootcamp.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)