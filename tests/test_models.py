#!/usr/bin/env python3
import pytest


from logging_configuration.models import Logger, Filter, Handler

def test__logger_creates_correct_dictionary():
    logger = Logger(name='logger', level='a level', propagate=True, filters=[], handlers=[])

    assert logger.definition == {
        'level': 'a level',
        'propagate': True,
        'filters': [],
        'handlers': []
    }

def test__filter_creates_correct_dictionary():
    returner = lambda x: x
    filterator = Filter(name='filter', logger_name='logger', filter_callable=returner)

    assert filterator.definition == {
        'logger_name': 'logger',
        'filter_callable': returner
    }

def test__handler_created_correct_dictionary():
    handler = Handler(name='handler')
