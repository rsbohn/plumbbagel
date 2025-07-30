

from plumbbagel.engine import Engine
from plumbbagel.rules import RuleSet

rules_file = "/workspaces/plumbbagel/artifacts/rules/rules.json"
rules = RuleSet.from_file(rules_file)
engine = Engine(
    rules,
    dry_run=False,
    verbose=False,
    trace=True,
    explain=True

)

engine.process([{"text": "fish"}])