"""
This is a generic abstract class for a 3D shape.
TODO: This class can be expanded to include many other features, including but not limited to, surface area, etc.
"""

from abc import abstractmethod

from shape.shape import Shape

class ThreeDimensionalShape(Shape):
    """
    An abstract class to represent a generic 3D shape.
    """

    @abstractmethod
    def volume(self):
        pass