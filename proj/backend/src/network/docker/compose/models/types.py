"""
Common types defined for Docker Compose values
"""

from typing import Literal
from dataclasses import dataclass
import re

Value = str | int | float | bool | None


BYTE_VALUE_UNITS = Literal[
    "b", Literal["k", "kb"], Literal["m", "mb"], Literal["g", "gb"]
]


@dataclass
class ByteValue:
    """
    Representation of a byte value.
    """

    value: int
    unit: BYTE_VALUE_UNITS


DURATION_UNITS = Literal["us", "ms", "s", "m", "h"]


@dataclass
class Duration:
    """
    Representation of a duration.
    """

    microseconds: int
    milliseconds: int
    seconds: int
    minutes: int
    hours: int

    @classmethod
    def from_string(cls, duration_str: str):
        """
        Parse a duration from a string.
        """
        duration = Duration.zero()

        pattern = r"(?:(\d+)(us|ms|s|m|h))"
        matches: list[tuple[str, DURATION_UNITS]] = re.findall(pattern, duration_str)

        for value, unit in matches:
            value = int(value)
            if unit == "us":
                duration.microseconds += value
            elif unit == "ms":
                duration.milliseconds += value
            elif unit == "s":
                duration.seconds += value
            elif unit == "m":
                duration.minutes += value
            elif unit == "h":
                duration.hours += value

        # Convert accumulated values to higher units (carry-over)
        duration.minutes += duration.seconds // 60
        duration.seconds %= 60
        duration.hours += duration.minutes // 60
        duration.minutes %= 60

        return duration

    @staticmethod
    def zero():
        """
        Returns a duration that is the same as zero.
        """

        return Duration(0, 0, 0, 0, 0)
