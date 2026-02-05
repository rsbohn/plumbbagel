import json
from typing import Iterable

from .parser import read_messages
from .rules import RuleSet


class Engine:
    def __init__(self, rules: RuleSet, dry_run: bool = False, verbose: bool = False, trace: bool = False, explain: bool = False, json_output: bool = False):
        self.rules = rules
        self.dry_run = dry_run
        self.verbose = verbose
        self.trace = trace
        self.explain = explain
        self.json_output = json_output

    def _log(self, event_type: str, **data):
        """Log an event, either as JSON or human-readable text"""
        if self.json_output:
            output = {"event": event_type, **data}
            print(json.dumps(output))
        else:
            # Human-readable output based on event type
            if event_type == "rule_check":
                if self.trace:
                    print(f"Checking rule '{data['rule']}' against {data['message']}")
            elif event_type == "rule_match":
                if self.verbose or self.explain:
                    print(f"Rule '{data['rule']}' matched message {data['message']}")
            elif event_type == "rule_no_match":
                if self.trace:
                    print(f"Rule '{data['rule']}' did not match")
            elif event_type == "no_rules_matched":
                if self.verbose or self.explain:
                    print(f"No rule matched message {data['message']}")
            elif event_type == "action_dry_run":
                print(f"DRY RUN: would execute '{data['action']}'")
            elif event_type == "action_executed":
                print(data['action'])

    def process(self, lines: Iterable[str]):
        messages = read_messages(lines)
        for msg in messages:
            matched = False
            for rule in self.rules.rules:
                self._log("rule_check", rule=rule.name, message=msg.attributes)
                if rule.matches(msg):
                    matched = True
                    self._log("rule_match", rule=rule.name, message=msg.attributes, action=rule.action)
                    if self.dry_run:
                        self._log("action_dry_run", action=rule.action)
                    else:
                        self._log("action_executed", action=rule.action)
                    break
                else:
                    self._log("rule_no_match", rule=rule.name)
            if not matched:
                self._log("no_rules_matched", message=msg.attributes)
