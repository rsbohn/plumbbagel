import unittest
from io import StringIO
import sys
import json
from contextlib import contextmanager
from plumbbagel.engine import Engine
from plumbbagel.rules import RuleSet, Rule
from plumbbagel.message import Message


@contextmanager
def captured_stdout():
    """Context manager to safely capture stdout"""
    old_stdout = sys.stdout
    try:
        sys.stdout = StringIO()
        yield sys.stdout
    finally:
        sys.stdout = old_stdout


class EngineTests(unittest.TestCase):
    def test_engine_dry_run(self):
        """Test that dry_run mode doesn't execute actions"""
        rules = RuleSet([Rule(name='test', match={'cmd': 'test'}, action='echo test')])
        engine = Engine(rules, dry_run=True)
        
        with captured_stdout() as output:
            engine.process([{'cmd': 'test'}])
            result = output.getvalue()
        
        self.assertIn('DRY RUN', result)
        self.assertIn('echo test', result)

    def test_engine_verbose(self):
        """Test that verbose mode shows rule matching details"""
        rules = RuleSet([Rule(name='test', match={'cmd': 'test'}, action='echo test')])
        engine = Engine(rules, verbose=True)
        
        with captured_stdout() as output:
            engine.process([{'cmd': 'test'}])
            result = output.getvalue()
        
        self.assertIn('matched', result.lower())

    def test_engine_trace(self):
        """Test that trace mode shows each rule check"""
        rules = RuleSet([
            Rule(name='first', match={'cmd': 'other'}, action='echo other'),
            Rule(name='second', match={'cmd': 'test'}, action='echo test')
        ])
        engine = Engine(rules, trace=True, dry_run=True)
        
        with captured_stdout() as output:
            engine.process([{'cmd': 'test'}])
            result = output.getvalue()
        
        self.assertIn("Checking rule 'first'", result)
        self.assertIn("did not match", result)
        self.assertIn("Checking rule 'second'", result)

    def test_engine_no_match(self):
        """Test behavior when no rules match"""
        rules = RuleSet([Rule(name='test', match={'cmd': 'test'}, action='echo test')])
        engine = Engine(rules, verbose=True)
        
        with captured_stdout() as output:
            engine.process([{'cmd': 'nomatch'}])
            result = output.getvalue()
        
        self.assertIn('No rule matched', result)

    def test_engine_multiple_messages(self):
        """Test processing multiple messages"""
        rules = RuleSet([
            Rule(name='hello', match={'cmd': 'hello'}, action='echo Hello'),
            Rule(name='bye', match={'cmd': 'bye'}, action='echo Bye')
        ])
        engine = Engine(rules, dry_run=True)
        
        with captured_stdout() as output:
            engine.process([{'cmd': 'hello'}, {'cmd': 'bye'}])
            result = output.getvalue()
        
        self.assertIn('echo Hello', result)
        self.assertIn('echo Bye', result)

    def test_engine_json_output(self):
        """Test that JSON output mode produces valid JSON with correct event types"""
        rules = RuleSet([Rule(name='test', match={'cmd': 'test'}, action='echo test')])
        engine = Engine(rules, json_output=True, dry_run=True)
        
        with captured_stdout() as output:
            engine.process([{'cmd': 'test'}])
            result = output.getvalue()
        
        # Parse each line as JSON
        lines = result.strip().split('\n')
        for line in lines:
            data = json.loads(line)
            self.assertIn('event', data)
        
        # Check that we got the expected events
        events = [json.loads(line)['event'] for line in lines]
        self.assertIn('rule_check', events)
        self.assertIn('action_dry_run', events)  # Updated to check for specific dry_run event


if __name__ == '__main__':
    unittest.main()
