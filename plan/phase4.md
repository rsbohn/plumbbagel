# Phase 4: Developer Tooling 🧰

This phase introduces utilities, inspection tools, and early testing infrastructure to support plumbbagel development and debugging.

## Goals

- Provide visibility into routing decisions and message flow
- Help developers test plumbs and rule files quickly
- Lay groundwork for more advanced routing features

---

## Tasks

- [ ] **Write `plumbaggage(1)` inspection tool**  
      Reads plumb messages and reports metadata, route matches, and potential issues.  
      Can be humorous, strict, or informative depending on `--shame-level`.

- [ ] **Implement logging and tracing in `plumbbagel`**  
      Verbose output for each rule evaluation and action. Optional structured logs.

- [ ] **Support `--dry-run` mode**  
      Evaluate and display routing decisions without executing actions.

- [ ] **Add CLI flags for testing and introspection**  
      `--explain`, `--trace`, `--highlight`, etc.

- [ ] **Create reusable test plumb messages**  
      Stored in `tests/messages/` or similar.

- [ ] **Add unit tests for rule evaluation**  
      Focus on matcher logic, template expansion, fallback behavior.

- [ ] **Design integration test harness (`plumbtest`)**  
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
