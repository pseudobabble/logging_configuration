#!/usr/bin/env python3
from unittest.mock import Mock

import pytest

from logging_configuration.models import Logger, Filter, Handler, Formatter


def test__logger_creates_correct_dictionary():
    logger = Logger(
        name="logger", level="a level", propagate=True, filters=[], handlers=[]
    )

    assert logger.definition == {
        "level": "a level",
        "propagate": True,
        "filters": [],
        "handlers": [],
    }


def test__filter_creates_correct_dictionary():
    returner = lambda x: x
    filterator = Filter(name="filter", logger_name="logger", filter_callable=returner)

    assert filterator.definition == {
        "logger_name": "logger",
        "filter_callable": returner,
    }


def test__handler_creates_correct_dictionary():
    mock_formatter = Mock()
    handler = Handler(
        name="handler",
        level="level",
        handler_class="handler class",
        formatter=mock_formatter,
        filters=[],
    )

    assert handler.definition == {
        "level": "level",
        "class": "handler class",
        "formatter": mock_formatter,
        "filters": [],
    }


def test__formatter_creates_correct_dictionary():
    formatter = Formatter(
        name="formatter",
        output_format="format",
        date_format="date format",
    )

    assert formatter.definition == {
        'format': 'format',
        'date_fmt': 'date format'
    }
