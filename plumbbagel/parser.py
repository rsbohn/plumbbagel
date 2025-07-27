from typing import Iterable, List

from .message import Message


def read_messages(lines: Iterable[str]) -> List[Message]:
    """Read messages from an iterable of lines."""
    return [Message.from_line(line) for line in lines if line.strip()]
