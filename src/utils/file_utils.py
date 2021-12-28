""" This is a helper module with functions related to files
"""
from pathlib import Path


def exists(file_path):
    """
    exists(file)
        Checks if the file_path exists

    Parameters
    ----------
    file_path
        A path to a file

    Returns
    -------
    bool
        Returns True if the file exists and False otherwise
    """
    path = Path(file_path)
    return path.is_file()


def get_extension(file_path):
    """
    get_extension(file)
        Gets the extension of the given file.

    Parameters
    ----------
    file_path
        A path to a file

    Returns
    -------
    str
        Returns the extension of the file if it exists or None otherwise.
        The Returning extension contains a dot. Ex: .csv
    """
    if exists(file_path):
        return Path(file_path).suffix
    else:
        return None


def validate_extension(file_path, extension):
    """
    validate_extension(file_path)
        Gets the extension of the given file.

    Parameters
    ----------
    file_path
        A path to a file

    Returns
    -------
    str
        Returns the extension of the file if it exists or None otherwise.
        The Returning extension contains a dot. Ex: .csv
    """
    return get_extension(file_path) == extension
