"""Utility module for common functions."""

import os


def get_tmp_path() -> str:
    """
    Get the path to the temporary directory.

    :return: The path to the temporary directory.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    tmp_folder_path = os.path.join(project_root, 'tmp')

    return tmp_folder_path
