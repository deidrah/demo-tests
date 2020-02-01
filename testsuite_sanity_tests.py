import unittest
from lost_hat_login_page_tests import LostHatLoginPageTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    # adding test classes:
    test_suite.addTest(LostHatLoginPageTests('test_correct_login'))
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(sanity_suite())