"""
Utility functions for working with SQL files.

Functions:
    load_sql: Load a SQL file from disk.

Exceptions:
    PathNotSpecifiedException: Raised when a path is not specified.
"""

import os

from typing import Optional

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class PathNotSpecifiedException(Exception):
    """Exception raised when a path is not specified."""
    pass

def load_sql(abs_path: Optional[str] = None, rel_path: Optional[str] = None) -> str:
    """Load a SQL file from disk.

    Args:
        path: The path to the SQL file.
    
    Returns:
        The contents of the SQL file.
    """
    if abs_path is not None:
        with open(abs_path, "r") as f:
            return f.read()
    elif rel_path is not None:
        with open(os.path.join(CURRENT_DIR, rel_path), "r") as f:
            return f.read()
    else:
        raise PathNotSpecifiedException("You must specify either an absolute or relative path.")