#!/usr/bin/env python3
import pytest

from logging_configuration.models import Logger

def test_logger_creates_correct_dictionary():
    logger = Logger(name='logger', level='a level', propagate=True, filters=[], handlers=[])

    assert logger.definition == {
        'level': 'a level',
        'propagate': True,
        'filters': [],
        'handlers': []
    }
