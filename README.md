# Foo Parameterization

A repository Foo, currently being used for calculating the volume of a sphere. This module can be extended to calculate the volume of more shapes (cylinder, cone, and cube) and build out the existing features.

## Environment
- Python 3.11.7

## Installation

Installing `foo` is simple. Just run the following command:
```
pip install .
```

## Usage

To determine the volume of a sphere in Python, you can use the following code:
```python
from foo import foo
my_foo = foo.Foo()
my_foo.sphere_calculate_volume_given_radius(3)
```

The application supports command line arguments. To calculate the volume of a sphere, you can use the following command:
```
python foo.py --radius=10 --volume
```
In this example the provided radius is 10 and the volume flag is provided to calculate the volume of the sphere.

## Testing
To run tests, use the following command:
```
python -m unittest discover tests
```

## Contributing
To contribute to this project, please refer to the `CONTRIBUTING.md` file.
