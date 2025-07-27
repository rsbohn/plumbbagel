from dataclasses import dataclass
from typing import Dict

@dataclass
class Message:
    """Represents a plumbbagel message."""

    attributes: Dict[str, str]

    @classmethod
    def from_line(cls, line: str) -> "Message":
        """Parse a simple key=value comma separated line into a Message."""
        attrs = {}
        line = line.strip()
        if not line:
            return cls(attrs)
        for part in line.split(','):
            if '=' in part:
                key, value = part.split('=', 1)
                attrs[key.strip()] = value.strip()
        return cls(attrs)
