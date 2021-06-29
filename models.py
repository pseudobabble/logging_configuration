#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List
from abc import ABC, abstractmethod


class LoggingDefinition:

    @property
    @abstractmethod
    def definition(self) -> dict:
        raise NotImplementedError(f'You must implement `definition` on {self.__class__.__name__}')

@dataclass
class Filter:
    pass

@dataclass
class Handler:
    pass

@dataclass
class Logger:
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
