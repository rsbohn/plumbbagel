# Phase 4: Developer Tooling 🧰

This phase introduces utilities, inspection tools, and early testing infrastructure to support plumbbagel development and debugging.

## Goals

- Provide visibility into routing decisions and message flow
- Help developers test plumbs and rule files quickly
- Lay groundwork for more advanced routing features

---

## Tasks

- [x] **Write `plumbaggage(1)` inspection tool**  
      Reads plumb messages and reports metadata, route matches, and potential issues.  
      Can be humorous, strict, or informative depending on `--shame-level`.

- [x] **Implement logging and tracing in `plumbbagel`**  
      Verbose output for each rule evaluation and action. Optional structured logs via `--json`.

- [x] **Support `--dry-run` mode**  
      Evaluate and display routing decisions without executing actions.

- [x] **Add CLI flags for testing and introspection**  
      `--explain`, `--trace`, `--highlight`, `--json` implemented.

- [x] **Create reusable test plumb messages**  
      Stored in `tests/messages/` (hello, bye, multi-attr, error, batch).

- [x] **Add unit tests for rule evaluation**  
      25 comprehensive tests covering matcher logic, parsing, engine modes.

- [x] **Design integration test harness (`plumbtest`)**  
      Feed message + rule + expected action into CLI, compare output.

---

## Optional / Stretch

- [ ] Output to HTML or structured UI (for debugging)
- [ ] Generate message flow diagrams
- [ ] Experimental features: `--hole`, `--toast-level`, `--therapy-mode`

---

## Philosophy

This is where the tools start talking back. Think `linter meets bartender` — helpful, mildly judgmental, deeply invested in your success.

---

## Linked Issues

(To be linked from GitHub or project board as created.)

---

## Implementation Summary

All core Phase 4 tasks have been completed. See `phase4-implementation-summary.md` for details.
