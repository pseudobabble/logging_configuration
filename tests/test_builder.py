#!/usr/bin/env python3
from unittest.mock import Mock

import pytest

from logging_configuration.builder import LoggingConfigurationBuilder
from logging_configuration.models import Formatter, Handler, Logger


def test__build_formatters_builds_correctly():
    mock_filters = [Mock()]
    mock_formatters = [Mock()]
    mock_handlers = [Mock()]
    mock_loggers = [Mock()]

    builder = LoggingConfigurationBuilder(
        mock_loggers, mock_formatters, mock_handlers, mock_filters
    )
