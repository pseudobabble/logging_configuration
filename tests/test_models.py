#!/usr/bin/env python3
from unittest.mock import Mock

import pytest

from logging_configuration.models import Logger, Filter, Handler, Formatter


def test__logger_creates_correct_dictionary():
    mock_filter1 = Mock()
    mock_filter1.name = 'filter1'
    mock_filter2 = Mock()
    mock_filter2.name = 'filter2'
    mock_filters = [mock_filter1, mock_filter2]

    mock_handler1 = Mock()
    mock_handler1.name = 'handler1'
    mock_handler2 = Mock()
    mock_handler2.name = 'handler2'
    mock_handlers = [mock_handler1, mock_handler2]

    logger = Logger(
        name="logger", level="a level", propagate=True, filters=mock_filters, handlers=mock_handlers
    )

    assert logger.definition == {
        "level": "a level",
        "propagate": True,
        "filters": ['filter1', 'filter2'],
        "handlers": ['handler1', 'handler2'],
    }


def test__filter_creates_correct_dictionary():
    returner = lambda x: x
    filterator = Filter(name="filter", logger_name="logger", filter_callable=returner)

    assert filterator.definition == {
        "logger_name": "logger",
        "filter_callable": returner,
    }


def test__handler_creates_correct_dictionary():
    formatter = Formatter(name='formatter', output_format='{message}', date_format='%Y-%m-%d', validate=False)

    mock_filter1 = Mock()
    mock_filter1.name = 'filter1'
    mock_filter2 = Mock()
    mock_filter2.name = 'filter2'

    handler = Handler(
        name="handler",
        level="level",
        handler_class="handler class",
        formatter=formatter,
        filters=[mock_filter1, mock_filter2],
    )

    assert handler.definition == {
        "level": "level",
        "class": "handler class",
        "formatter": formatter.name,
        "filters": ['filter1', 'filter2'],
    }


def test__formatter_creates_correct_dictionary():
    formatter = Formatter(
        name="formatter",
        output_format="format",
        date_format="date format",
        validate=False
    )

    assert formatter.definition == {"format": "format", "date_fmt": "date format", 'validate': False}
