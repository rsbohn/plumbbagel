# Quickstart

Get a minimal plumbbagel rules engine run in a few minutes.

## Prerequisites

- Python 3.8+

## 1) Install (editable)

From the repo root:

```bash
python -m pip install -e .
```

You can also run the CLI via `python -m` without installing.

## 2) Run the sample rules

The repo ships with a tiny rules file and message examples.

```bash
python -m plumbbagel sample.pbgl tests/messages/hello.txt
```

You should see output for the `hello` rule action.

## 3) Pass a message inline

You can provide a message line directly instead of a file:

```bash
python -m plumbbagel sample.pbgl "cmd=bye"
```

## 4) Read from stdin

If you omit the message argument, plumbbagel reads from stdin:

```bash
echo "cmd=hello" | python -m plumbbagel sample.pbgl
```

## 5) Debug a rule match

Use verbose, trace, or explain flags to see why a rule matched (or didn’t):

```bash
python -m plumbbagel sample.pbgl tests/messages/error.txt --trace
python -m plumbbagel sample.pbgl tests/messages/error.txt --explain
```

## Next steps

- Inspect messages with `plumbaggage`:

```bash
python -m plumbbagel.plumbaggage sample.pbgl tests/messages/hello.txt
```

- Write your own `.pbgl` rules:

```json
{
  "rules": [
    {"name": "ok", "match": {"status": "ok"}, "action": "echo OK"}
  ]
}
```
