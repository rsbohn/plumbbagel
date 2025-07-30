from typing import Iterable, List

from .message import Message


def read_messages(lines: Iterable[str]) -> List[Message]:
    """Read messages from an iterable of lines."""
    messages = []
    for line in lines:
        if isinstance(line, dict):
            # Accept dicts directly as Message attributes
            messages.append(Message(line))
        elif isinstance(line, str) and line.strip():
            messages.append(Message.from_line(line))
    return messages
