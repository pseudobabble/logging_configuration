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
    filters = [filter1, filter2]

    mock_formatters = [Mock()]
    mock_handlers = [Mock()]
    mock_loggers = [Mock()]

    builder = LoggingConfigurationBuilder(
        mock_loggers, mock_formatters, mock_handlers, filters
    )

    assert builder.build_filter_definitions() == {
        'filter1': filter1.definition,
        'filter2': filter2.definition
   }

def test__builder_builds_formatters_correctly():
    mock_filters = [Mock()]

    formatter1 = Formatter(name='formatter1', output_format='some format 1', date_format='date format 1')
    formatter2 = Formatter(name='formatter2', output_format='some format 2', date_format='date format 2')
    formatters = [formatter1, formatter2]

    mock_handlers = [Mock()]
    mock_loggers = [Mock()]

    builder = LoggingConfigurationBuilder(
        mock_loggers, formatters, mock_handlers, mock_filters
    )

    assert builder.build_formatter_definitions() == {
        'formatter1': formatter1.definition,
        'formatter2': formatter2.definition
    }
