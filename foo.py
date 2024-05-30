"""
Package that calculates Foo for spheres.

Author: Charles Thomas

Execute this script with the following command:
```
python foo.py
```

"""

import argparse
from shape.three_dimensional.sphere import Sphere

ERROR = -1

"""Helper functions."""
def sphere_calculate_volume_given_radius(radius):
    """
    Calculate the volume of a sphere with the given radius.

    Parameters
    ----------
    radius : float
        The radius of the sphere.

    Returns
    -------
    float : The volume of the sphere.
    """

    print(f"Calculating the volume of a sphere with radius {radius}.")
    
    try:
        sphere = Sphere(radius)
        return sphere.volume()
    except ValueError as exception:
        print(exception)
    return ERROR

def add_args():
    """
    Add arguments to the argument parser.
    You can add more arguments here as needed.
    """
    # Parse the radius from the command line.
    # Note: The radius must be a positive float.
    # More arguments can be added here. ie. --volume, --surface_area, etc.
    # When adding new features, be sure to add a test for it in tests/test_sphere.py.
    argument_parser = argparse.ArgumentParser(description="Calculate Foo for a sphere.")
    argument_parser.add_argument("--radius", dest="radius", required=True, type=float, help="The radius of the sphere.")
    argument_parser.add_argument("--volume", action="store_true", help="Calculate the volume of the sphere.")
    argument_parser.add_argument("--surface-area", action="store_true", help="Calculate the volume of the sphere.") # not functional yet
    return argument_parser.parse_args()

def main():
    """
    Main function.
    """
    args = add_args()
    if args.volume:
        volume = sphere_calculate_volume_given_radius(args.radius)
        if volume != ERROR:
            print(f"The volume of the sphere with radius {args.radius} is {volume} cubic units.") # using cubic units for now. See TODO in sphere.py.
    if args.surface_area: # TODO: Implement surface area calculation and others below here.
        print("Surface area calculation not implemented.")
        pass

if __name__ == '__main__':
    main()