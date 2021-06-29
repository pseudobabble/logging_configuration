#!/usr/bin/env python3
from typing import List

from logging_configuration.models import Logger

class LoggingConfigurationBuilder:

    def __init__(self, loggers: List[Logger]):
        self.loggers = loggers
