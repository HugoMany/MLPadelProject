import os
import pandas as pd


def readAllFileVibration(folderPath):
    """
    Reads all CSV files from a given folder and its subfolders, and returns their data along with the folder names.

    Args:
        folderPath (str): The path to the folder containing the CSV files.

    Returns:
        list of tuple: A list of tuples where each tuple contains:
            - folder_name (str): The name of the folder containing the CSV file.
            - df (pandas.DataFrame): The data from the CSV file as a pandas DataFrame.

    Example:
        folderPath = "/path/to/folder"
        data = readAllFileVibration(folderPath)
        print(data[0]) #folder_name
        print(data[1]) #df
    """
    csv_data = []
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)
                folder_name = os.path.basename(root)
                df = pd.read_csv(file_path)
                csv_data.append((folder_name, df))
    return csv_data