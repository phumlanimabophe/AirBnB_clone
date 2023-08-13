#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
# import json
import pep8
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os


class TestConsoleClass(unittest.TestCase):
    """TestConsoleClass resume
    Args:
        unittest (): Propertys for unit testing
    """

    maxDiff = None

    # Define a test case setup method to set up conditions for testing file saving.
    def setUp(self):
        """ condition to test file saving """
        # Open "test.json" in write mode, effectively clearing its content.
        with open("test.json", 'w'):
            # Update the file path attribute of FileStorage to point to "test.json".
            FileStorage._FileStorage__file_path = "test.json"
            # Initialize the objects dictionary attribute of FileStorage as an empty dictionary.
            FileStorage._FileStorage__objects = {}

    # Define a test case method to test the 'quit' command of the console.
    def test_quit(self):
        # Capture the standard output using a StringIO object.
        with patch('sys.stdout', new=StringIO()) as f:
            # Run the 'onecmd' method of the console to execute the 'quit' command.
            self.assertTrue(self.console.onecmd("quit"))  # Check if the command returns True.
            # Assert that the captured output (stdout) is an empty string.
            self.assertEqual(f.getvalue().strip(), "")

    # Define a test case method to test the 'create' command of the console.
    def test_create(self):
        # Capture the standard output using a StringIO object.
        with patch('sys.stdout', new=StringIO()) as f:
            # Run the 'onecmd' method of the console to execute the 'create' command for a 'BaseModel' instance.
            self.console.onecmd("create BaseModel")
            # Get the captured output.
            output = f.getvalue().strip()
            # Check if the length of the output (presumably the ID) is 36 characters.
            self.assertTrue(len(output) == 36)

    # Define a test case method to test the 'show' command of the console.
    def test_show(self):
        # Capture the standard output using a StringIO object.
        with patch('sys.stdout', new=StringIO()) as f:
            # Run the 'onecmd' method of the console to execute the 'show' command for a non-existing instance.
            self.console.onecmd("show BaseModel 1234-1234-1234")
            # Get the captured output.
            output = f.getvalue().strip()
            # Assert that the output matches the "** no instance found **" message.
            self.assertEqual(output, "** no instance found **")

if __name__ == '__main__':
    unittest.main()
