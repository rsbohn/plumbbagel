import json
import re
from dataclasses import dataclass
from typing import Any, Dict, List

from .message import Message


class _SafeDict(dict):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


@dataclass
class Rule:
    name: str
    match: Dict[str, str]
    action: str  # for prototype just a string to print

    def matches(self, msg: Message) -> bool:
        for k, v in self.match.items():
            value = msg.attributes.get(k)
            if value is None:
                return False
            if isinstance(v, str) and v.startswith("re:"):
                pattern = v[3:]
                if re.fullmatch(pattern, value) is None:
                    return False
            elif value != v:
                return False
        return True

    def render_action(self, attrs: Dict[str, str]) -> str:
        return self.action.format_map(_SafeDict(attrs))


class RuleSet:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    @classmethod
    def from_file(cls, path: str) -> "RuleSet":
        with open(path) as fh:
            data = json.load(fh)
        rules = [Rule(**r) for r in data.get("rules", [])]
        return cls(rules)
