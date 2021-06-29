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
        version: int = 1,
        incremental: bool = False,
        disable_existing_loggers: bool = True
    ) -> None:
        self.loggers = loggers
        self.formatters = formatters
        self.handlers = handlers
        self.filters = filters
        self.version = version
        self.incremental = incremental
        self.disable_existing_loggers = disable_existing_loggers

    def build_filter_definitions(self) -> dict:
        return {filterator.name: filterator.definition for filterator in self.filters}

    def build_formatter_definitions(self) -> dict:
        return {formatter.name: formatter.definition for formatter in self.formatters}

    def build_handler_definitions(self) -> dict:
        return {handler.name: handler.definition for handler in self.handlers}

    def build_logger_definitions(self) -> dict:
        return {logger.name: logger.definition for logger in self.loggers}

    def build_logging_configuration(self) -> dict:
        return {
            'version': self.version,
            'incremental': self.incremental,
            'disable_existing_loggers': self.disable_existing_loggers,
            'loggers': self.build_logger_definitions(),
            'handlers': self.build_handler_definitions(),
            'formatters': self.build_formatter_definitions(),
            'filters': self.build_filter_definitions()
        }
