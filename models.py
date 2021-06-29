#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List, Union, Callable
from abc import ABC, abstractmethod
from logging import Filter


class LoggingDefinition:

    @property
    @abstractmethod
    def definition(self) -> dict:
        raise NotImplementedError(f'You must implement `definition` on {self.__class__.__name__}')

@dataclass
class Filter(LoggingDefinition):
    name: str
    logger_name: str
    filter_callable: Union[Callable, Filter]

    @property
    def definition(self):
        return {
            'logger_name': self.logger_name,
            'filter_callable': self.filter_callable
        }


@dataclass
class Handler(LoggingDefinition):
    name: str

    @property
    def definition(self):
        pass

@dataclass
class Logger(LoggingDefinition):
    name: str
    level: str
    propagate: bool
    filters: List[Filter]
    handlers: List[Handler]

    @property
    def definition(self):
        return {
            'level': self.level,
            'propagate': self.propagate,
            'filters': self.filters,
            'handlers': self.handlers
        }
