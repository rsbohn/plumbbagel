import unittest
from io import StringIO
import sys
import json
from plumbbagel.engine import Engine
from plumbbagel.rules import RuleSet, Rule
from plumbbagel.message import Message


class EngineTests(unittest.TestCase):
    def test_engine_dry_run(self):
        """Test that dry_run mode doesn't execute actions"""
        rules = RuleSet([Rule(name='test', match={'cmd': 'test'}, action='echo test')])
        engine = Engine(rules, dry_run=True)
        
        # Capture output
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        engine.process([{'cmd': 'test'}])
        output = sys.stdout.getvalue()
        
        sys.stdout = old_stdout
        
        self.assertIn('DRY RUN', output)
        self.assertIn('echo test', output)

    def test_engine_verbose(self):
        """Test that verbose mode shows rule matching details"""
        rules = RuleSet([Rule(name='test', match={'cmd': 'test'}, action='echo test')])
        engine = Engine(rules, verbose=True)
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        engine.process([{'cmd': 'test'}])
        output = sys.stdout.getvalue()
        
        sys.stdout = old_stdout
        
        self.assertIn('matched', output.lower())

    def test_engine_trace(self):
        """Test that trace mode shows each rule check"""
        rules = RuleSet([
            Rule(name='first', match={'cmd': 'other'}, action='echo other'),
            Rule(name='second', match={'cmd': 'test'}, action='echo test')
        ])
        engine = Engine(rules, trace=True, dry_run=True)
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        engine.process([{'cmd': 'test'}])
        output = sys.stdout.getvalue()
        
        sys.stdout = old_stdout
        
        self.assertIn("Checking rule 'first'", output)
        self.assertIn("did not match", output)
        self.assertIn("Checking rule 'second'", output)

    def test_engine_no_match(self):
        """Test behavior when no rules match"""
        rules = RuleSet([Rule(name='test', match={'cmd': 'test'}, action='echo test')])
        engine = Engine(rules, verbose=True)
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        engine.process([{'cmd': 'nomatch'}])
        output = sys.stdout.getvalue()
        
        sys.stdout = old_stdout
        
        self.assertIn('No rule matched', output)

    def test_engine_multiple_messages(self):
        """Test processing multiple messages"""
        rules = RuleSet([
            Rule(name='hello', match={'cmd': 'hello'}, action='echo Hello'),
            Rule(name='bye', match={'cmd': 'bye'}, action='echo Bye')
        ])
        engine = Engine(rules, dry_run=True)
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        engine.process([{'cmd': 'hello'}, {'cmd': 'bye'}])
        output = sys.stdout.getvalue()
        
        sys.stdout = old_stdout
        
        self.assertIn('echo Hello', output)
        self.assertIn('echo Bye', output)

    def test_engine_json_output(self):
        """Test that JSON output mode produces valid JSON"""
        rules = RuleSet([Rule(name='test', match={'cmd': 'test'}, action='echo test')])
        engine = Engine(rules, json_output=True)
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        engine.process([{'cmd': 'test'}])
        output = sys.stdout.getvalue()
        
        sys.stdout = old_stdout
        
        # Parse each line as JSON
        lines = output.strip().split('\n')
        for line in lines:
            data = json.loads(line)
            self.assertIn('event', data)
        
        # Check that we got the expected events
        events = [json.loads(line)['event'] for line in lines]
        self.assertIn('rule_check', events)
        self.assertIn('action', events)


if __name__ == '__main__':
    unittest.main()
