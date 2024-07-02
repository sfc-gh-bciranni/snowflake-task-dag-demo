"""
This module contains functions for authenticating to Snowflake using either environment variables or a local configuration file.

Functions:
    authenticate_from_env: Authenticate to Snowflake using environment variables.
    authenticate_from_local: Authenticate to Snowflake using a local configuration file.
    authenticate: Authenticate to Snowflake using either environment variables or a local configuration file.
"""

import os
from snowflake.snowpark import Session

def authenticate_from_env() -> Session:
    """Authenticate to Snowflake using environment variables."""
    connection_params = {
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "role": os.getenv("SNOWFLAKE_ROLE"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA"),
    }
    return Session.builder.configs(connection_params).create()


def authenticate_from_local(connection_name: str) -> Session:
    """Authenticate to Snowflake using a local configuration TOML file stored at ~/.snowflake/connections/.

    Args:
        connection_name: The name of the connection in the local configuration file.

    Returns:
        A Snowpark session object.
    """
    return Session.builder.config("connection_name", connection_name).create()


def authenticate(local: bool = False, connection_name: str = None) -> Session:
    """Authenticate to Snowflake using either environment variables or a local configuration file.

    Args:
        local: Whether to use a local configuration file.
        connection_name: The name of the connection in the local configuration file.

    Returns:
        A Snowpark session object.
    """
    if local:
        return authenticate_from_local(connection_name)
    return authenticate_from_env()