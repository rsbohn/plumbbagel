

from plumbbagel.engine import Engine

rules = "./artifacts/fishtest/rules.json"
engine = Engine(
    rules,
    dry_run=False,
    verbose=False,
    trace=False,
    explain=True

)

engine.process("fish")