#!/usr/bin/env python3
import pytest

from logging_configuration.builder import LoggingConfigurationBuilder

def test__build_formatters_builds_correctly():
    builder = LoggingConfigurationBuilder()
