import argparse
import json
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
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parsed = parser.parse_args(args)

    rules = RuleSet.from_file(parsed.rules)
    engine = Engine(
        rules,
        dry_run=parsed.dry_run,
        verbose=parsed.verbose,
        trace=parsed.trace,
        explain=parsed.explain,
        json_output=parsed.json,
    )

    if parsed.message:
        # Check if file exists first to avoid ambiguity
        if os.path.exists(parsed.message):
            # Read from file
            with open(parsed.message) as fh:
                lines = [line for line in fh if line.strip()]
        elif '=' in parsed.message:
            # Direct message on command line
            lines = [parsed.message]
        else:
            # Assume it's a file that doesn't exist - let it fail naturally
            with open(parsed.message) as fh:
                lines = [line for line in fh if line.strip()]
    else:
        # Read from stdin
        lines = [line for line in open(0) if line.strip()]

    engine.process(lines)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
