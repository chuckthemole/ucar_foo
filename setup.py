from setuptools import setup, find_packages

REQUIRED_PACKAGES = []

setup(
    name='foo',
    version='0.1',
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    author='Charles Thomas',
    author_email='chuckthemole@gmail.com',
    description='A package for calculating the Foo for spheres.',
    url='https://github.com/chuckthemole/ucar_foo.git',
    classifiers=['Programming Language :: Python :: 3'],
    python_requires='>=3.6',
)
