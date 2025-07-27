import unittest
from plumbbagel.message import Message
from plumbbagel.rules import Rule, RuleSet

class RuleTests(unittest.TestCase):
    def test_rule_match(self):
        rule = Rule(name='hello', match={'cmd':'hello'}, action='echo hi')
        msg = Message({'cmd':'hello'})
        self.assertTrue(rule.matches(msg))

    def test_rule_no_match(self):
        rule = Rule(name='hello', match={'cmd':'hello'}, action='echo hi')
        msg = Message({'cmd':'bye'})
        self.assertFalse(rule.matches(msg))

    def test_ruleset_from_file(self):
        ruleset = RuleSet.from_file('sample.pbgl')
        self.assertEqual(len(ruleset.rules), 2)
        self.assertEqual(ruleset.rules[0].name, 'hello')

if __name__ == '__main__':
    unittest.main()
