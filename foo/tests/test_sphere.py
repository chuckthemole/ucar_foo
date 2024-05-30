import unittest
from shape.three_dimensional.sphere import Sphere

class TestSphere(unittest.TestCase):
    """
    A class to test the Sphere class.
    """

    """Initialization tests."""
    def test_init_positive_radius(self):
        sphere_radius_1 = Sphere(1)
        sphere_radius_3 = Sphere(3)
        self.assertEqual(sphere_radius_1.radius, 1)
        self.assertEqual(sphere_radius_3.radius, 3)
    
    def test_init_zero_radius(self):
        sphere_radius_0 = Sphere(0)
        self.assertEqual(sphere_radius_0.radius, 0)
    
    def test_init_negative_radius(self):
        with self.assertRaises(ValueError) as context:
            Sphere(-1)
        self.assertTrue("Error: radius is less than 0." in str(context.exception))

    """Volume tests."""
    def test_volume_positive_radius(self):
        sphere_radius_1 = Sphere(1)
        sphere_radius_3 = Sphere(3)
        self.assertEqual(round(sphere_radius_1.volume(), 5), 4.18879)
        self.assertEqual(round(sphere_radius_3.volume(), 5), 113.09734)

    def test_volume_zero_radius(self):
        sphere_radius_0 = Sphere(0)
        self.assertAlmostEqual(sphere_radius_0.volume(), 0)

    def test_volume_negative_radius(self):
        with self.assertRaises(ValueError):
            Sphere(-1).volume()

    """Add other tests below here. ie Surface area tests, etc."""

if __name__ == '__main__':
    unittest.main()
