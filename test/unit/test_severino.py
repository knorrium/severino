import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'severino'))
from severino import severino

class testSeverino(unittest.TestCase):
    
    def test_default_values(self):
        sev = severino.Severino()
        self.assertEqual(True, sev.is_ok)
        self.assertEqual(None, sev.base)
        self.assertEqual(None, sev.current)

# TODO: too tired to patch it now
#    def test_compare_must_be_able_to_override_default_values(self):
        

    def test_severino_should_receive_revision_and_check_differences(self):
        sev = severino.Severino(base="test/resources/good_rev/*", current="test/resources/bad_rev/*")
        sev.compare()
        self.assertTrue(sev.is_ok)

    def test_alternative_sad_path(self):
        sev = severino.Severino(current="./test/resources/bad_rev/*")
        #sev.take_screenshots()
        diffs = sev.compare(base="./test/resources/good_rev/*")
        self.assertEqual(['./test/resources/bad_rev/chrome-yahoo.png'], diffs)

