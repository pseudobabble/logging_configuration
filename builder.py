#!/usr/bin/env python3
from typing import List

from logging_configuration.models import Logger, Formatter, Handler, Filter


class LoggingConfigurationBuilder:
    def __init__(
        self,
        loggers: List[Logger],
        formatters: List[Formatter],
        handlers: List[Handler],
        filters: List[Filter],
    ):
        self.loggers = loggers
        self.formatters = formatters
        self.handlers = handlers
        self.filters = filters
