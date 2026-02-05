# Feature Complete Plan for plumbbagel

**Date:** 2026-02-05  
**Status:** Phase 4 (Developer Tooling) - 60% Complete  
**Goal:** Achieve feature complete status for plumbbagel rules engine

---

## Current State

### ✅ Completed (Phase 1-3)
- Core rules engine with basic message routing
- JSON-based rule format (`.pbgl` files)
- CLI with dry-run, verbose, explain, and trace modes
- Message parser for `key=value` format
- Basic plumbaggage inspection tool
- Basic plumbtest integration test runner
- Sample messages and tests

### 🚧 In Progress (Phase 4)
- Developer tooling infrastructure exists but incomplete
- Limited test coverage (4 unit tests)
- Basic exact-match rule evaluation only
- No advanced pattern matching or template expansion

---

## Three-Step Plan to Feature Complete

### **Step 1: Complete Phase 4 Developer Tooling** 🧰

**Goal:** Finish all core Phase 4 tasks from `plan/phase4.md`

#### Tasks:
1. **Enhanced plumbaggage Inspection Tool**
   - Add detailed rule matching analysis (which rules matched, which didn't, why)
   - Show message attribute breakdown
   - Implement all shame levels with useful feedback
   - Add `--json` output format for structured data

2. **Structured Logging & Tracing**
   - Add proper logging infrastructure to engine.py
   - Implement structured log output (JSON format option)
   - Enhance `--trace` to show each rule evaluation step
   - Add `--explain` detailed output with matching logic

3. **Comprehensive Unit Tests**
   - Test matcher logic with various rule patterns
   - Test message parsing edge cases
   - Test CLI flag combinations
   - Achieve >80% code coverage

4. **Integration Tests**
   - Test all CLI modes (dry-run, verbose, trace, explain)
   - Test with multiple message formats
   - Test error conditions and edge cases
   - Add test runner documentation

**Deliverables:**
- Fully functional plumbaggage and plumbtest tools
- Complete test suite with good coverage
- Enhanced debugging capabilities
- Clear developer documentation

---

### **Step 2: Advanced Matching & Template Expansion** 🎯

**Goal:** Add flexible pattern matching and dynamic action generation

#### Tasks:
1. **Pattern Matching in Rules**
   - Implement wildcard matching (`*`, `?`)
   - Add regex pattern support (with `/pattern/` syntax)
   - Support negation patterns (`!value`)
   - Add range matching for numeric values

2. **Template Expansion**
   - Implement variable substitution in action strings
   - Support `${attribute}` syntax for message attributes
   - Add default values: `${attribute:-default}`
   - Handle missing attributes gracefully

3. **Fallback & Default Rules**
   - Add `default: true` rule attribute for catch-all rules
   - Implement rule priority/ordering
   - Add "no match" handling with customizable behavior

4. **Tests for New Features**
   - Unit tests for each matching type
   - Template expansion edge cases
   - Fallback behavior validation
   - Complex rule combination tests

**Deliverables:**
- Flexible rule matching system
- Dynamic action generation from message attributes
- Fallback/default rule handling
- Updated sample.pbgl with advanced examples

---

### **Step 3: Polish & Documentation** 📚

**Goal:** Production-ready documentation and user experience

#### Tasks:
1. **Code Documentation**
   - Add comprehensive docstrings to all functions
   - Document rule format and matching semantics
   - Add inline comments for complex logic
   - Generate API documentation

2. **User Documentation**
   - Expand README with:
     - Installation instructions
     - Quick start guide
     - Rule syntax reference
     - CLI usage examples
   - Create `docs/` directory with:
     - User guide
     - Developer guide
     - Rule format specification
     - Advanced examples

3. **Example Collection**
   - Create `examples/` directory
   - Add common use case examples
   - Include annotated rule files
   - Add sample integration scenarios

4. **Final Testing & Edge Cases**
   - Stress test with large rule files
   - Test with malformed input
   - Verify all error messages are helpful
   - Performance testing and optimization

**Deliverables:**
- Complete user and developer documentation
- Rich example collection
- Production-ready error handling
- Comprehensive test coverage

---

## What Remains Unclear or Unspecified

### Critical Clarifications Needed:

#### 1. **Pattern Matching Semantics**
**Question:** What pattern matching capabilities should rules support?

**Options:**
- A) Simple wildcards only (`*`, `?`) - easiest to implement
- B) Full regex support - most flexible but complex
- C) Both with different syntaxes - balanced approach
- D) Glob patterns (shell-style) - familiar to users

**Recommendation:** Option C - wildcards by default, regex with `/pattern/` syntax

---

#### 2. **Template Expansion Syntax**
**Question:** What syntax should be used for variable substitution in actions?

**Options:**
- A) Shell-style: `$var` or `${var}`
- B) Python-style: `{var}` or `%(var)s`
- C) Custom syntax: `{{var}}` or `<<var>>`
- D) No templates, use JSON action objects instead

**Recommendation:** Option A - `${var}` is familiar and supports defaults `${var:-default}`

---

#### 3. **Fallback Strategy**
**Question:** How should rules handle messages that don't match any rule?

**Options:**
- A) Silent failure (no action)
- B) Error/warning message
- C) Single default/fallback rule
- D) Priority-based cascading with explicit default
- E) Configurable per-ruleset

**Recommendation:** Option E - configurable with sensible default (warn and take no action)

---

#### 4. **Action Execution Capabilities**
**Question:** Should actions support shell features like pipes and redirects?

**Options:**
- A) Simple command execution only (secure, predictable)
- B) Full shell execution (flexible but security risk)
- C) Predefined action types (echo, log, exec, etc.)
- D) Plugin/extension system for custom actions

**Current:** A (simple execution)  
**Recommendation:** Keep A initially, document C as future enhancement

---

#### 5. **Performance & Scale Requirements**
**Question:** What are the performance expectations?

**Considerations:**
- Number of rules per file: 10s, 100s, 1000s?
- Message throughput: messages/second target?
- Real-time vs batch processing?
- Memory constraints?

**Recommendation:** Document that current implementation is proof-of-concept; optimize if needed after real-world usage

---

#### 6. **Stretch Goals Scope**
**Question:** Are Phase 4 stretch goals in scope for "feature complete"?

**Stretch goals from phase4.md:**
- `--hole` flag
- `--toast-level` flag
- `--therapy-mode` flag
- HTML/structured UI output
- Message flow diagrams

**Recommendation:** Exclude from "feature complete" - these are experimental/fun features. Document as future enhancements.

---

## Assumptions Made

For this plan, the following assumptions are made:

1. **Feature complete = Phase 4 core tasks completed**
   - Stretch goals and experimental features are optional
   - Focus on production-ready core functionality

2. **Current JSON rule format is stable**
   - `.pbgl` files use JSON structure
   - Schema can be extended but not fundamentally changed

3. **Simple template expansion sufficient**
   - No need for complex DSL or scripting language
   - Basic variable substitution and conditionals adequate

4. **Pattern matching: wildcards first, regex optional**
   - Start with simple glob-style patterns
   - Add regex support if needed based on feedback

5. **Python 3.8+ target**
   - No need for backwards compatibility with older Python
   - Can use modern Python features

6. **CLI-focused, no GUI**
   - Command-line tool is primary interface
   - Web UI or graphical tools out of scope

7. **Security: sandboxed execution**
   - Actions should not have unrestricted shell access
   - Consider running actions in restricted environment

8. **Single-user, local execution**
   - Not building a distributed system
   - No need for authentication or authorization

---

## Success Criteria

Feature complete is achieved when:

- ✅ All Phase 4 core tasks are implemented and tested
- ✅ Pattern matching and template expansion work reliably
- ✅ Test coverage is >80% with comprehensive integration tests
- ✅ Documentation is complete (README, user guide, API docs)
- ✅ Example collection demonstrates key use cases
- ✅ All CLI flags work as documented
- ✅ Error handling is robust and user-friendly
- ✅ Code is well-documented with docstrings
- ✅ Tool can be installed and used by external users

---

## Out of Scope (Post Feature Complete)

Items explicitly NOT included in feature complete:

- GUI or web interface
- Distributed/networked operation
- Advanced action types (HTTP requests, database operations)
- Configuration file format beyond JSON
- Internationalization/localization
- Plugin system
- Performance optimization beyond basic needs
- Stretch goals (`--hole`, `--toast-level`, `--therapy-mode`)

---

## Timeline Estimate

**Step 1 (Developer Tooling):** ~40% of effort
- Already 60% complete, finish remaining items
- Focus: testing infrastructure and debugging tools

**Step 2 (Advanced Features):** ~40% of effort  
- New functionality: pattern matching, templates
- Most complex technical implementation

**Step 3 (Polish & Documentation):** ~20% of effort
- Important but straightforward
- Builds on completed work

**Total:** Estimated 20-30 hours of focused development

---

## Next Steps

1. **Get clarification** on unspecified items (especially pattern matching and templates)
2. **Begin Step 1** with enhanced plumbaggage tool
3. **Iterate** on each task with frequent testing
4. **Review** after each step to adjust plan as needed

---

**Note:** This is a living document. Update as requirements become clearer and implementation reveals new insights.
