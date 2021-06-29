#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List


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
