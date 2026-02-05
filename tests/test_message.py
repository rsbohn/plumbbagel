import unittest
from plumbbagel.message import Message
from plumbbagel.parser import read_messages


class MessageTests(unittest.TestCase):
    def test_message_from_line_simple(self):
        """Test parsing simple key=value message"""
        msg = Message.from_line('cmd=hello')
        self.assertEqual(msg.attributes, {'cmd': 'hello'})

    def test_message_from_line_multiple_attrs(self):
        """Test parsing message with multiple attributes"""
        msg = Message.from_line('cmd=hello,user=alice')
        self.assertEqual(msg.attributes, {'cmd': 'hello', 'user': 'alice'})

    def test_message_from_line_with_spaces(self):
        """Test parsing message with spaces around separators"""
        msg = Message.from_line('cmd = hello , user = alice')
        self.assertEqual(msg.attributes, {'cmd': 'hello', 'user': 'alice'})

    def test_message_from_line_empty(self):
        """Test parsing empty message"""
        msg = Message.from_line('')
        self.assertEqual(msg.attributes, {})

    def test_message_from_line_no_equals(self):
        """Test parsing message without equals sign"""
        msg = Message.from_line('just text')
        self.assertEqual(msg.attributes, {})

    def test_message_from_line_with_equals_in_value(self):
        """Test parsing message with equals in value"""
        msg = Message.from_line('cmd=test=value')
        self.assertEqual(msg.attributes, {'cmd': 'test=value'})

    def test_read_messages_from_strings(self):
        """Test reading messages from string lines"""
        lines = ['cmd=hello', 'cmd=bye']
        messages = read_messages(lines)
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0].attributes, {'cmd': 'hello'})
        self.assertEqual(messages[1].attributes, {'cmd': 'bye'})

    def test_read_messages_from_dicts(self):
        """Test reading messages from dict objects"""
        lines = [{'cmd': 'hello'}, {'cmd': 'bye'}]
        messages = read_messages(lines)
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0].attributes, {'cmd': 'hello'})
        self.assertEqual(messages[1].attributes, {'cmd': 'bye'})

    def test_read_messages_skip_empty_lines(self):
        """Test that empty lines are skipped"""
        lines = ['cmd=hello', '', '  ', 'cmd=bye']
        messages = read_messages(lines)
        self.assertEqual(len(messages), 2)


class RuleMatcherTests(unittest.TestCase):
    def test_exact_match(self):
        """Test exact attribute matching"""
        from plumbbagel.rules import Rule
        rule = Rule(name='test', match={'cmd': 'hello'}, action='echo hi')
        msg = Message({'cmd': 'hello'})
        self.assertTrue(rule.matches(msg))

    def test_no_match_different_value(self):
        """Test no match when value differs"""
        from plumbbagel.rules import Rule
        rule = Rule(name='test', match={'cmd': 'hello'}, action='echo hi')
        msg = Message({'cmd': 'bye'})
        self.assertFalse(rule.matches(msg))

    def test_no_match_missing_key(self):
        """Test no match when key is missing"""
        from plumbbagel.rules import Rule
        rule = Rule(name='test', match={'cmd': 'hello'}, action='echo hi')
        msg = Message({'other': 'value'})
        self.assertFalse(rule.matches(msg))

    def test_multiple_attributes_match(self):
        """Test matching multiple attributes"""
        from plumbbagel.rules import Rule
        rule = Rule(name='test', match={'cmd': 'hello', 'user': 'alice'}, action='echo hi')
        msg = Message({'cmd': 'hello', 'user': 'alice'})
        self.assertTrue(rule.matches(msg))

    def test_multiple_attributes_partial_match(self):
        """Test that partial matches fail"""
        from plumbbagel.rules import Rule
        rule = Rule(name='test', match={'cmd': 'hello', 'user': 'alice'}, action='echo hi')
        msg = Message({'cmd': 'hello', 'user': 'bob'})
        self.assertFalse(rule.matches(msg))

    def test_extra_attributes_in_message(self):
        """Test that extra attributes in message don't prevent match"""
        from plumbbagel.rules import Rule
        rule = Rule(name='test', match={'cmd': 'hello'}, action='echo hi')
        msg = Message({'cmd': 'hello', 'extra': 'data'})
        self.assertTrue(rule.matches(msg))


if __name__ == '__main__':
    unittest.main()
