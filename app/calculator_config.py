# app/calculator_config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


class ConfigError(Exception):
    pass


class CalculatorConfig:
    def __init__(self):
        self.history_file = os.getenv('HISTORY_FILE')
        self.validate()

    def validate(self):
        if not self.history_file or not isinstance(self.history_file, str):
            raise ConfigError(
                "HISTORY_FILE environment variable must be set to a valid file path.")
