from typing import Iterable

from .parser import read_messages
from .rules import RuleSet


class Engine:
    def __init__(self, rules: RuleSet, dry_run: bool = False, verbose: bool = False, trace: bool = False, explain: bool = False):
        self.rules = rules
        self.dry_run = dry_run
        self.verbose = verbose
        self.trace = trace
        self.explain = explain

    def process(self, lines: Iterable[str]):
        messages = read_messages(lines)
        for msg in messages:
            matched = False
            for rule in self.rules.rules:
                if self.trace:
                    print(f"Checking rule '{rule.name}' against {msg.attributes}")
                if rule.matches(msg):
                    matched = True
                    if self.verbose or self.explain:
                        print(f"Rule '{rule.name}' matched message {msg.attributes}")
                    if not self.dry_run:
                        print(rule.action)
                    else:
                        print(f"DRY RUN: would execute '{rule.action}'")
                    break
                else:
                    if self.trace:
                        print(f"Rule '{rule.name}' did not match")
            if not matched:
                if self.verbose or self.explain:
                    print(f"No rule matched message {msg.attributes}")
