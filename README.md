# plumbbagel

plumbbagel is a simple rules engine prototype. The project is currently 
under development and serves as a proof of concept. Expect rough edges and
rapid iteration.

## Goals
- Provide a lightweight rules evaluation engine.
- Experiment with flexible rule syntax.
- Serve as a playground for future improvements.

More documentation will be added as the codebase evolves.

## Developer Tools

Phase 4 introduces helper utilities for debugging and testing:

### plumbbagel - Main CLI

The main command-line interface for routing messages.

```bash
python -m plumbbagel <rules.pbgl> <message>
```

**Options:**
- `-n, --dry-run` - Show actions without executing them
- `-v, --verbose` - Show detailed rule matching information
- `--trace` - Trace each rule check (shows all rule evaluations)
- `--explain` - Explain rule evaluation decisions
- `--json` - Output structured JSON logs for programmatic processing

**Examples:**
```bash
# Process a message file with dry-run
python -m plumbbagel sample.pbgl tests/messages/hello.txt --dry-run

# Trace rule evaluation
python -m plumbbagel sample.pbgl tests/messages/hello.txt --trace

# Get JSON output for log processing
python -m plumbbagel sample.pbgl tests/messages/hello.txt --json
```

### plumbaggage - Message Inspector

Inspect plumb messages and see which rules they match. Can provide helpful (or judgmental) feedback.

```bash
python -m plumbbagel.plumbaggage <rules.pbgl> <message>
```

**Options:**
- `--shame-level <none|mild|harsh>` - How judgmental to be about unmatched messages
- `--trace` - Trace rule evaluation

**Examples:**
```bash
# Inspect a message
python -m plumbbagel.plumbaggage sample.pbgl tests/messages/hello.txt

# Be judgmental about unmatched messages
python -m plumbbagel.plumbaggage sample.pbgl tests/messages/error.txt --shame-level=harsh
```

### plumbtest - Integration Test Runner

Run integration tests to verify that rules produce expected output.

```bash
python -m plumbbagel.plumbtest <rules.pbgl> <message> <expected_output>
```

**Example:**
```bash
# Test that hello message produces correct output
python -m plumbbagel.plumbtest sample.pbgl tests/messages/hello.txt "echo Hello"
```

## Message Format

Messages are simple key=value pairs:
```
cmd=hello
cmd=hello,user=alice
status=error,code=404
```

## Rule Format

Rules are defined in JSON format (`.pbgl` files):
```json
{
  "rules": [
    {"name": "hello", "match": {"cmd": "hello"}, "action": "echo Hello"},
    {"name": "bye", "match": {"cmd": "bye"}, "action": "echo Bye"}
  ]
}
```

## Testing

Run the test suite:
```bash
python -m unittest discover tests/
```

## Authors

Randall Bohn <rsbohn@gmail.com>