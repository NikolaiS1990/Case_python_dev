import unittest
from unittest.mock import mock_open, patch
import json
from ..load_data import JSONLoader 

class TestJSONLoader(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment.
        """
        self.loader = JSONLoader()

    def test_load_json_success(self):
        """
        Test if JSONLoader successfully loads valid JSON data.
        """
        mock_json_content = '{"key": "value"}'
        with patch("builtins.open", mock_open(read_data=mock_json_content)):
            result = self.loader.load_json("mock_path.json")
            self.assertEqual(result, {"key": "value"})

    def test_load_json_file_not_found(self):
        """
        Test if JSONLoader raises FileNotFoundError for a missing file.
        """
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                self.loader.load_json("non_existent_file.json")

    def test_load_json_invalid_json(self):
        """
        Test if JSONLoader raises JSONDecodeError for invalid JSON content.
        """
        invalid_json_content = "{key: value"  # Missing quotes and incorrect format
        with patch("builtins.open", mock_open(read_data=invalid_json_content)):
            with self.assertRaises(json.JSONDecodeError):
                self.loader.load_json("invalid.json")

    def test_load_json_empty_file(self):
        """
        Test if JSONLoader raises JSONDecodeError for an empty JSON file.
        """
        empty_json_content = ""
        with patch("builtins.open", mock_open(read_data=empty_json_content)):
            with self.assertRaises(json.JSONDecodeError):
                self.loader.load_json("empty.json")

    def test_load_json_unicode_content(self):
        """
        Test if JSONLoader correctly loads JSON with Unicode characters.
        """
        unicode_json_content = '{"message": "Hello, 🌍!"}'
        with patch("builtins.open", mock_open(read_data=unicode_json_content)):
            result = self.loader.load_json("unicode.json")
            self.assertEqual(result, {"message": "Hello, 🌍!"})

if __name__ == "__main__":
    unittest.main()
