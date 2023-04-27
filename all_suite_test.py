import unittest



from test_cases.login_to_the_system import TestLogInPage
from test_cases.zad4_test import TestCase01


def full_suite():
    test_loader = unittest.TestLoader()

    test_suite = unittest.TestSuite()
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestLogInPage))
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestCase01))

    new_test_suite = unittest.TestSuite()
    new_test_suite.addTests(test_suite)

    test_names = []
    for test in new_test_suite:
        if isinstance(test, unittest.TestCase):
            test_names.append(str(test))
        else:
            for sub_test in test:
                test_names.append(str(sub_test))

    unittest.TextTestRunner().run(test_suite)

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())