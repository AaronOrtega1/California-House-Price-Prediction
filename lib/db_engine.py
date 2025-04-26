import os
from dotenv import load_dotenv
from typing import List, Optional, Dict


class DatabaseEngine:
    def __init__(self, env_conf: List[str], defaults: Optional[Dict[str, str]] = None):
        """Initialize the conexión to the database loading the env variables.

        Args:
            env_conf (List[str]): List of env variables to load.
                Ex: ["DB_USER", "DB_PASSWORD", "DB_HOST", "DB_PORT", "DB_NAME"]
        """

        load_dotenv()
        self.defaults = defaults or {}
        self.env_vars = self._load_env_variable(env_conf)

    def _load_env_variable(self, env_conf: List[str]) -> Dict[str, str]:
        """Loads the env variables specified in the list.

        Args:
            env_conf (List[str]): List of env variables to load.

        Returns:
            Dict[str, str]: Dictionary with the loaded variables.

        Raises:
            RuntimeError: If a variable is not define or doesn't have a default value.
        """
        env_vars = {}
        for var_name in env_conf:
            value = os.getenv(var_name, self.defaults.get(var_name))
            if value is None:
                raise RuntimeError(
                    f"The env variable '{var_name}' is not define and doesn't have a default value."
                )
            env_vars[var_name] = value
        return env_vars

    def get_connection_string(self) -> str:
        """Generates the string connection

        Returns:
            str: Connection string.

        Raises:
            RuntimeError: If there are missing variables required for the string.
        """
        try:
            engine_str = f"postgresql://{self.env_vars['DB_USER']}:{self.env_vars['DB_PASSWORD']}@{self.env_vars.get('DB_HOST', 'postgres')}:{self.env_vars.get('DB_PORT', '5432')}/{self.env_vars.get('DB_NAME', 'housing_db')}"
            return engine_str
        except KeyError as e:
            raise RuntimeError(f"Variable required for the connection not found: {e}")

    def generate_engine(self):
        from sqlalchemy import create_engine

        return create_engine(self.get_connection_string())
