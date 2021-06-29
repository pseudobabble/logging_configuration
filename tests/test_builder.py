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
        filter1.name: filter1.definition,
        filter2.name: filter2.definition
   }

def test__builder_builds_formatters_correctly():
    mock_filters = [Mock()]

    formatter1 = Formatter(name='formatter1', output_format='some format 1', date_format='date format 1', validate=False)
    formatter2 = Formatter(name='formatter2', output_format='some format 2', date_format='date format 2', validate=False)
    formatters = [formatter1, formatter2]

    mock_handlers = [Mock()]
    mock_loggers = [Mock()]

    builder = LoggingConfigurationBuilder(
        mock_loggers, formatters, mock_handlers, mock_filters
    )

    assert builder.build_formatter_definitions() == {
        formatter1.name: formatter1.definition,
        formatter2.name: formatter2.definition
    }

def test__builder_builds_handlers_correctly():
    filter_callable_1 = lambda x: x
    filter_callable_2 = lambda x: x
    filter1 = Filter(name='filter1', logger_name="", filter_callable=filter_callable_1)
    filter2 = Filter(name='filter2', logger_name="", filter_callable=filter_callable_2)
    filters = [filter1, filter2]

    formatter1 = Formatter(name='formatter1', output_format='some format 1', date_format='date format 1', validate=False)
    formatter2 = Formatter(name='formatter2', output_format='some format 2', date_format='date format 2', validate=False)
    formatters = [formatter1, formatter2]

    handler1 = Handler(name='handler1', level='level1', handler_class='handler class 1', formatter=formatter1, filters=filters)
    handler2 = Handler(name='handler2', level='level2', handler_class='handler class 2', formatter=formatter2, filters=filters)
    handlers = [handler1, handler2]

    mock_loggers = [Mock()]

    builder = LoggingConfigurationBuilder(
        mock_loggers, formatters, handlers, filters
    )

    assert builder.build_handler_definitions() == {
        handler1.name: handler1.definition,
        handler2.name: handler2.definition
    }

def test__builder_builds_loggers_correctly():
    filter_callable_1 = lambda x: x
    filter_callable_2 = lambda x: x
    filter1 = Filter(name='filter1', logger_name="", filter_callable=filter_callable_1)
    filter2 = Filter(name='filter2', logger_name="", filter_callable=filter_callable_2)
    filters = [filter1, filter2]

    formatter1 = Formatter(name='formatter1', output_format='some format 1', date_format='date format 1', validate=False)
    formatter2 = Formatter(name='formatter2', output_format='some format 2', date_format='date format 2', validate=False)
    formatters = [formatter1, formatter2]

    handler1 = Handler(name='handler1', level='level1', handler_class='handler class 1', formatter=formatter1, filters=filters)
    handler2 = Handler(name='handler2', level='level2', handler_class='handler class 2', formatter=formatter2, filters=filters)
    handlers = [handler1, handler2]

    logger1 = Logger(name='logger1', level='level1', propagate=True, filters=filters, handlers=handlers)
    logger2 = Logger(name='logger2', level='level2', propagate=True, filters=filters, handlers=handlers)
    loggers = [logger1, logger2]

    builder = LoggingConfigurationBuilder(
        loggers, formatters, handlers, filters
    )

    assert builder.build_logger_definitions() == {
        logger1.name: logger1.definition,
        logger2.name: logger2.definition
    }

def test__build_logging_configuration_builds_correctly():
    filter_callable_1 = lambda x: x
    filter_callable_2 = lambda x: x
    filter1 = Filter(name='filter1', logger_name="", filter_callable=filter_callable_1)
    filter2 = Filter(name='filter2', logger_name="", filter_callable=filter_callable_2)
    filters = [filter1, filter2]

    formatter1 = Formatter(name='formatter1', output_format='some format 1', date_format='date format 1', validate=False)
    formatter2 = Formatter(name='formatter2', output_format='some format 2', date_format='date format 2', validate=False)
    formatters = [formatter1, formatter2]

    handler1 = Handler(name='handler1', level='level1', handler_class='handler class 1', formatter=formatter1, filters=filters)
    handler2 = Handler(name='handler2', level='level2', handler_class='handler class 2', formatter=formatter2, filters=filters)
    handlers = [handler1, handler2]

    logger1 = Logger(name='logger1', level='level1', propagate=True, filters=filters, handlers=handlers)
    logger2 = Logger(name='logger2', level='level2', propagate=True, filters=filters, handlers=handlers)
    loggers = [logger1, logger2]

    builder = LoggingConfigurationBuilder(
        loggers, formatters, handlers, filters
    )

    assert builder.build_logging_configuration() == {
        'version': 1,
        'incremental': False,
        'disable_existing_loggers': True,
        'loggers': {
            logger1.name: logger1.definition,
            logger2.name: logger2.definition
        },
        'handlers': {
            handler1.name: handler1.definition,
            handler2.name: handler2.definition
        },
        'formatters': {
            formatter1.name: formatter1.definition,
            formatter2.name: formatter2.definition
        },
        'filters': {
            filter1.name: filter1.definition,
            filter2.name: filter2.definition
        }
    }
