from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="conda_packager",
    version="1.0",
    author="Alex Ramos",
    description="A small example package",
    license='',
    packages=['conda_packager'],
    python_requires=">=3.8",
    url='',
    zip_safe=False
)