#!/usr/bin/env python3
import sys
import logging
import logging.config

import pytest

from logging_configuration.models import Filter, Formatter, StreamHandler, Logger
from logging_configuration.builder import LoggingConfigurationBuilder

def test__dictconfig_accepts_output(caplog):
    filter_callable_1 = 'logging.Filter'
    filter_callable_2 = 'logging.Filter'
    filter1 = Filter(name='filter1', logger_name="", filter_callable=filter_callable_1)
    filter2 = Filter(name='filter2', logger_name="logger1", filter_callable=filter_callable_2)
    filters = [filter1, filter2]

    formatter1 = Formatter(name='formatter1', output_format='{message}', date_format='%Y-%m-%d', validate=False)
    formatter2 = Formatter(name='formatter2', output_format='{message}', date_format='%Y-%m-%d', validate=False)
    formatters = [formatter1, formatter2]

    handler1 = StreamHandler(name='handler1', level='DEBUG', handler_class='logging.StreamHandler', formatter=formatter1, filters=filters, stream=sys.stdout)
    handler2 = StreamHandler(name='handler2', level='DEBUG', handler_class='logging.StreamHandler', formatter=formatter2, filters=filters, stream=sys.stdout)
    handlers = [handler1, handler2]

    logger1 = Logger(name='logger1', level='DEBUG', propagate=True, filters=filters, handlers=handlers)
    logger2 = Logger(name='logger2', level='DEBUG', propagate=True, filters=filters, handlers=handlers)
    loggers = [logger1, logger2]

    builder = LoggingConfigurationBuilder(
        loggers, formatters, handlers, filters
    )

    logging.config.dictConfig(builder.build_logging_configuration())
    logger1_instance = logging.getLogger('logger1')
    logger1_instance.debug('logger1 here, over.')

    logger2_instance = logging.getLogger('logger2')
    logger2_instance.debug('Loud and clear logger1, over.')

    print(caplog.record_tuples)
    assert caplog.record_tuples[0] == ('logger1', 10, 'logger1 here, over.')
    assert caplog.record_tuples[1] == ('logger2', 10, 'Loud and clear logger1, over.')

    assert True
