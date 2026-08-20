"""Time interval parsing for the timer."""

import re


_DURATION_PATTERN = re.compile(r"^(?P<value>\d+(?:\.\d+)?)(?P<unit>[smh])$")

_UNIT_TO_SECONDS = {
    "s": 1,
    "m": 60,
    "h": 60 * 60,
}


class InvalidDurationError(ValueError):
    """Raised when a timer duration cannot be parsed."""


def parse_duration(value: str) -> float:
    """Convert a duration such as ``5s``, ``25m`` or ``1h`` to seconds."""
    if not value:
        raise InvalidDurationError("Timer duration cannot be empty.")

    match = _DURATION_PATTERN.fullmatch(value.strip().lower())

    if match is None:
        raise InvalidDurationError(
            "Invalid timer duration. Use a value such as 5s, 25m or 1h."
        )

    number = float(match.group("value"))
    unit = match.group("unit")

    seconds = number * _UNIT_TO_SECONDS[unit]

    if seconds <= 0:
        raise InvalidDurationError("Timer duration must be greater than zero.")

    return seconds