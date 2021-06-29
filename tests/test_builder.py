#!/usr/bin/env python3
from unittest.mock import Mock

import pytest

from logging_configuration.builder import LoggingConfigurationBuilder


def test__build_formatters_builds_correctly():
    mock_formatters = [Mock()]
    mock_handlers = [Mock()]
    mock_loggers = [Mock()]

    builder = LoggingConfigurationBuilder(mock_loggers, mock_formatters, mock_handlers)
