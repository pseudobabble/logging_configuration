#!/usr/bin/env python3
import pytest

from logging_configuration.models import Logger

def test_logger_creates_correct_dictionary():
    logger = Logger(level='a level')
