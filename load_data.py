"""This utility class loads and parses JSON files."""

import json

class JSONLoader:
    """
    A utility class to load and parse JSON files.
    """

    def load_json(self, dictionary_path: str) -> dict:
        """
        Loads a JSON file and returns its content.

        Parameters:
            file_path (str): The path to the JSON file.

        Returns:
            dict: Parsed content of the JSON file.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """

        try:
            with open(dictionary_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except FileNotFoundError as error:
            print(f"Error: The file '{dictionary_path}' was not found.")
            raise error
        except json.JSONDecodeError as error:
            print(f"Error: Failed to decode JSON from the file '{dictionary_path}'.")
            raise error
