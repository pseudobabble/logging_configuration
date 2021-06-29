#!/usr/bin/env python3
import pytest


from logging_configuration.models import Logger, Filter

def test_logger_creates_correct_dictionary():
    logger = Logger(name='logger', level='a level', propagate=True, filters=[], handlers=[])

    assert logger.definition == {
        'level': 'a level',
        'propagate': True,
        'filters': [],
        'handlers': []
    }

def test_filter_creates_correct_dictionary():
    returner = lambda x: x
    filterator = Filter(name='filter', filter_callable=returner)

    assert filterator.definition == {
        'filter_callable': returner
    }
