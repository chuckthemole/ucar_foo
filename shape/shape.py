"""
This is a generic abstract class for a shape.
TODO: This class can be expanded to include many other features.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    An abstract class to represent a generic shape.
    """

    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass