import unittest

from unittest.loader import makeSuite

from test_cases.login_to_the_system import TestLogInPage
from test_cases.add_player_assert import TestAddPlayer

def full_suite():
   test_suite = unittest.TestLoader()
   test_suite.loadTestsFromTestCase(TestLogInPage)
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
