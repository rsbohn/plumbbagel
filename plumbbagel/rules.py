import json
from dataclasses import dataclass
from typing import Any, Dict, List

from .message import Message


@dataclass
class Rule:
    name: str
    match: Dict[str, str]
    action: str  # for prototype just a string to print

    def matches(self, msg: Message) -> bool:
        for k, v in self.match.items():
            if msg.attributes.get(k) != v:
                return False
        return True


class RuleSet:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    @classmethod
    def from_file(cls, path: str) -> "RuleSet":
        data = json.load(open(path))
        rules = [Rule(**r) for r in data.get("rules", [])]
        return cls(rules)
