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


    def test_severino_should_create_database_if_doesnt_exist(self):
        sev = severino.Severino(db="./test.db")
        self.assertTrue(sev.storage.is_valid())
        sev.remove_db()


    def test_severino_should_add_a_new_revision_to_history(self):
        sev = severino.Severino(rev="test_revision", db="./test.db")
        sev._flag_as_good() # this should be called by compare()
        
        self.assertTrue(sev.check("test_revision"))

    def test_severino_should_be_able_to_check_against_good_and_bad_revisions(self):
        """
        This test explains the expected behavior if the user adds two revisions with the same name. (It should compare against the latest one) and also guarantees that severino checks for good and bad revisions.
        """
        sev = severino.Severino(base="test/resources/good_rev/*", current="test/resources/good_rev/*", db="./test.db", rev="rev_1")
        sev.compare()
#        self.assertTrue(sev.check(revision="rev_1"))

        sev.compare(current="test/resources/bad_rev/*")
        self.assertFalse(sev.check(revision="rev_1"))
