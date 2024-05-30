import math
try:
    from shape.three_dimensional.three_dimensional_shape import ThreeDimensionalShape
except ImportError:
    print("ImportError: Unable to import ThreeDimensionalShape from shape.three_dimensional.three_dimensional_shape")
    print("Trying to import ThreeDimensionalShape from foo.shape.three_dimensional.three_dimensional_shape")
    try:
        from foo.shape.three_dimensional.three_dimensional_shape import ThreeDimensionalShape
    except ImportError:
        print("ImportError: Unable to import ThreeDimensionalShape from foo.shape.three_dimensional.three_dimensional_shape")
        exit(1)

"""
This class provides functions to calculate aspects of a sphere.

If you add a new function to this class, be sure to add a test for it in tests/test_sphere.py.

TODO: Think about creating a CubicShape class that Sphere and Cube can inherit from, making a member variable 'units_type' that can be 'meters', 'feet', etc.
- update: I did create a Shape class and ThreeDimensionalShape class. The above todo can still be implemented. For now this class just inherits from ThreeDimensionalShape.
"""

class Sphere(ThreeDimensionalShape):
    """
    A class to represent a sphere.
    """

    def __init__(self, radius):
        """
        Initialize the sphere with the given radius.
        Note: The radius must be a positive float.

        Parameters
        ----------
        radius : float
            The radius of the sphere.
        """

        # Check if the radius is less than 0, if so, raise an error, otherwise set member variable.
        if radius < 0:
            raise ValueError("Error: radius is less than 0.")
        print(f"Creating a sphere with radius {radius}.")
        self.radius = radius
    
    def __str__(self):
        """
        Return a string representation of the sphere.

        Returns
        -------
        str : A string representation of the sphere.
        """

        return f"Sphere with radius {self.radius}."

    def volume(self):
        """
        Calculate the volume of a sphere with the given radius.

        Returns
        -------
        float : The volume of the sphere.
        """

        return (4.0/3.0) * math.pi * (self.radius**3)