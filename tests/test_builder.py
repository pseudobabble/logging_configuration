#!/usr/bin/env python3
from unittest.mock import Mock

import pytest

from logging_configuration.builder import LoggingConfigurationBuilder
from logging_configuration.models import Formatter, Handler, Logger, Filter


def test__build_formatters_initialises():
    mock_filters = [Mock()]
    mock_formatters = [Mock()]
    mock_handlers = [Mock()]
    mock_loggers = [Mock()]

    builder = LoggingConfigurationBuilder(
        mock_loggers, mock_formatters, mock_handlers, mock_filters
    )

def test__builder_builds_filters_correctly():
    filter_callable_1 = lambda x: x
    filter_callable_2 = lambda x: x

    filter1 = Filter(name='filter1', logger_name="", filter_callable=filter_callable_1)
    filter2 = Filter(name='filter2', logger_name="", filter_callable=filter_callable_1)

    mock_filters = [filter1, filter2]
    mock_formatters = [Mock()]
    mock_handlers = [Mock()]
    mock_loggers = [Mock()]

    builder = LoggingConfigurationBuilder(
        mock_loggers, mock_formatters, mock_handlers, mock_filters
    )

    assert builder.build_filter_definitions() == {
        'filter1': filter1.definition,
        'filter2': filter2.definition
   }
