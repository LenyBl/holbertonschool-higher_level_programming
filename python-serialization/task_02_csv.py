#!/bin/usr/python3
"""
This module contains a function to convert a CSV file to a JSON file.
"""
import csv
import json


def convert_csv_to_json(csv_file, json_file):
    """
    Converts a CSV file to a JSON file.
    Args:
        csv_file (str): The path to the input CSV file.
        json_file (str): The path to the output JSON file.
    Returns:
        None
    """
    try:
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open(json_file, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
    except (FileNotFoundError, csv.Error, json.JSONDecodeError) as e:
        print(f"Error: {e}")
