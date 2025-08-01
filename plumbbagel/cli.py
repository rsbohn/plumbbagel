import argparse
import os
from typing import List

from .engine import Engine
from .rules import RuleSet


def main(args: List[str] = None) -> int:
    parser = argparse.ArgumentParser(description="plumbbagel routing engine")
    parser.add_argument("rules", help="Path to .pbgl rules file")
    parser.add_argument("message", nargs="?", help="Message line. If omitted, read stdin")
    parser.add_argument("-n", "--dry-run", action="store_true", help="Show actions without executing")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--explain", action="store_true", help="Explain rule evaluation")
    parser.add_argument("--trace", action="store_true", help="Trace each rule check")
    parser.add_argument("--highlight", action="store_true", help="Highlight matches (no-op)")
    parsed = parser.parse_args(args)

    rules = RuleSet.from_file(parsed.rules)
    engine = Engine(
        rules,
        dry_run=parsed.dry_run,
        verbose=parsed.verbose,
        trace=parsed.trace,
        explain=parsed.explain,
    )

    if parsed.message:
        if '=' in parsed.message or not os.path.exists(parsed.message):
            # Wrap the message as a dict for matching rules expecting {"text": ...}
            lines = [{"text": parsed.message.strip()}]
        else:
            with open(parsed.message) as fh:
                lines = [ {"text": line.strip()} for line in fh if line.strip() ]
    else:
        lines = [ {"text": line.strip()} for line in open(0) if line.strip() ]

    engine.process(lines)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
