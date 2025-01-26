# utils.py
# Utility functions for common operations

import json

def read_json(file_path):
    """Reads a JSON file and returns its content."""
    with open(file_path, "r") as file:
        return json.load(file)

def save_json(data, file_path):
    """Writes data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
