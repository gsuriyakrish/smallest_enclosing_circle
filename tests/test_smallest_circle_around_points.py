"""
This module is for testing the
the smallest circle around a cluster of points in 2D
TODO : Cover more scenario in unittest
"""

import unittest
from smallest_circle import pilot
from os import path


class TestSmallestCircle(unittest.TestCase):
    def test_invalid_negative_input(self):
        """Test the invalid input data and then getting an error."""
        response = pilot(input_points=-1)
        self.assertEqual("Wrong input value...Value must be an Integer and should not have negative value",
                         response["error_description"])
        self.assertEqual("Error", response["message"])

    def test_invalid_character_input(self):
        """Test the invalid input data and then getting an error."""
        response = pilot(input_points="s")
        self.assertEqual("Wrong input value...Value must be an Integer and should not have negative value",
                         response["error_description"])
        self.assertEqual("Error", response["message"])

    def test_invalid_decimal_input(self):
        """Test the invalid input data and then getting an error."""
        response = pilot(input_points=1.0)
        self.assertEqual("Wrong input value...Value must be an Integer and should not have negative value",
                         response["error_description"])
        self.assertEqual("Error", response["message"])

    def test_output_parameter_message_6(self):
        """Test the output data with success message."""
        response = pilot(input_points=6)
        self.assertEqual("Success", response["message"])

    def test_output_parameter_centre_6(self):
        """Test the output data with graph_path."""
        response = pilot(input_points=6)
        self.assertEqual("Success", response["message"])
        self.assertTrue(response["centre"] != "")

    def test_output_parameter_radius_6(self):
        """Test the output data with graph_path."""
        response = pilot(input_points=6)
        self.assertEqual("Success", response["message"])
        #self.assertTrue(path.exists(response["graph_path"]) == True)
        self.assertTrue(response["graph_path"] != "")

    def test_output_parameter_input_points_6(self):
        """Test the output data with input_points."""
        response = pilot(input_points=6)
        self.assertEqual("Success", response["message"])
        self.assertTrue(len(response["input_points"]) == 6)

    def test_output_parameter_time_taken_6(self):
        """Test the output data with input_points."""
        response = pilot(input_points=6)
        self.assertEqual("Success", response["message"])
        self.assertTrue(response["time_taken"] != "")
