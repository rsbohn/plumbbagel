import subprocess
import sys
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(__file__))
PLUMBTEST = os.path.join(ROOT, 'plumbbagel', 'plumbtest.py')


class PlumbTestCase(unittest.TestCase):
    def test_plumbtest_pass(self):
        cmd = [sys.executable, PLUMBTEST, os.path.join(ROOT, 'sample.pbgl'), os.path.join(ROOT, 'tests/messages/hello.txt'), 'echo Hello']
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertIn('PASS', result.stdout)


if __name__ == '__main__':
    unittest.main()
