import argparse
from typing import List

from .engine import Engine
from .rules import RuleSet


def main(args: List[str] = None) -> int:
    parser = argparse.ArgumentParser(description="plumbbagel routing engine")
    parser.add_argument("rules", help="Path to .pbgl rules file")
    parser.add_argument("message", nargs="?", help="Message line. If omitted, read stdin")
    parser.add_argument("-n", "--dry-run", action="store_true", help="Show actions without executing")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parsed = parser.parse_args(args)

    rules = RuleSet.from_file(parsed.rules)
    engine = Engine(rules, dry_run=parsed.dry_run, verbose=parsed.verbose)

    if parsed.message:
        lines = [parsed.message]
    else:
        lines = [line for line in open(0)]

    engine.process(lines)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
