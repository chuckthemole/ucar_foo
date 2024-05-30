"""
This is a generic abstract class for a 3D shape.
TODO: This class can be expanded to include many other features, including but not limited to, surface area, etc.
"""

from abc import abstractmethod

try:
    from shape.shape import Shape
except ImportError:
    print("ImportError: Unable to import Shape from shape.shape")
    print("Trying to import Shape from foo.shape.shape")
    try:
        from foo.shape.shape import Shape
    except ImportError:
        print("ImportError: Unable to import Shape from foo.shape.shape")
        exit(1)

class ThreeDimensionalShape(Shape):
    """
    An abstract class to represent a generic 3D shape.
    """

    @abstractmethod
    def volume(self):
        pass