from typing import Iterable

from .parser import read_messages
from .rules import RuleSet


class Engine:
    def __init__(self, rules: RuleSet, dry_run: bool = False, verbose: bool = False):
        self.rules = rules
        self.dry_run = dry_run
        self.verbose = verbose

    def process(self, lines: Iterable[str]):
        messages = read_messages(lines)
        for msg in messages:
            matched = False
            for rule in self.rules.rules:
                if rule.matches(msg):
                    matched = True
                    if self.verbose:
                        print(f"Rule '{rule.name}' matched message {msg.attributes}")
                    if not self.dry_run:
                        print(rule.action)
                    else:
                        print(f"DRY RUN: would execute '{rule.action}'")
                    break
            if not matched and self.verbose:
                print(f"No rule matched message {msg.attributes}")
