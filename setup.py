from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='live_reload',
    version='1.0.0',
    packages=['live_reload'],
    description='A Python library for live reloading scripts on file changes.',
    author="CrypterENC",
    author_email="a95899003@gmail.com",
    url='https://github.com/CrypterENC/live_reload.git',
    python_requires=">=3.8",
    license="MIT",
)
