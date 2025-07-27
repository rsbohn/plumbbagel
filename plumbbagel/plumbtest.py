import argparse
import subprocess
import sys
from typing import List


def main(argv: List[str] = None) -> int:
    parser = argparse.ArgumentParser(description="Run plumbbagel integration test")
    parser.add_argument("rules")
    parser.add_argument("message")
    parser.add_argument("expected")
    parsed = parser.parse_args(argv)

    cmd = [sys.executable, '-m', 'plumbbagel.cli', parsed.rules, parsed.message, '--dry-run']
    result = subprocess.run(cmd, capture_output=True, text=True)

    output = result.stdout.strip()
    if parsed.expected in output:
        print("PASS")
        return 0
    else:
        print("FAIL")
        print(output)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
