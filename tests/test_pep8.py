import os
import unittest
import pycodestyle


class TestPep8(unittest.TestCase):
    defaults = {
        'repeat': True
    }

    def test_pep8(self):
        kwargs = self.defaults.copy()
        style = pycodestyle.StyleGuide(**kwargs)
        for root, dirs, files in os.walk('/'):
            python_files = [os.path.join(root, f) for f in files if f.endswith('.py')]
            style.check_files(python_files)
        n = style.check_files().total_errors
        self.assertEqual(n, 0, 'PEP8 style errors: %d' % n)
