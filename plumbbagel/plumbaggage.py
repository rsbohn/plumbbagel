import argparse
from typing import Iterable, List

from .parser import read_messages
from .rules import RuleSet
from .engine import Engine


def inspect_messages(rules: RuleSet, lines: Iterable[str], shame_level: str, trace: bool) -> None:
    engine = Engine(rules, dry_run=True, verbose=False, trace=trace)
    for msg in read_messages(lines):
        print(f"Message: {msg.attributes}")
        matched = False
        for rule in rules.rules:
            if rule.matches(msg):
                matched = True
                print(f"Matched rule '{rule.name}' -> {rule.action}")
                break
        if not matched:
            print("No rule matched")
        if shame_level != "none" and not matched:
            if shame_level == "mild":
                print("  Perhaps check your attributes?")
            elif shame_level == "harsh":
                print("  Shame! This message is lost in the ether!")


def main(args: List[str] = None) -> int:
    parser = argparse.ArgumentParser(description="Inspect plumbbagel messages")
    parser.add_argument("rules", help="Path to .pbgl rules file")
    parser.add_argument("message", nargs="?", help="Message line or file path")
    parser.add_argument("--shame-level", default="none", choices=["none", "mild", "harsh"], help="How judgmental to be")
    parser.add_argument("--trace", action="store_true", help="Trace rule evaluation")
    parsed = parser.parse_args(args)

    rules = RuleSet.from_file(parsed.rules)

    if parsed.message and '=' in parsed.message:
        lines = [parsed.message]
    elif parsed.message:
        lines = open(parsed.message)
    else:
        lines = [line for line in open(0)]

    inspect_messages(rules, lines, parsed.shame_level, parsed.trace)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
