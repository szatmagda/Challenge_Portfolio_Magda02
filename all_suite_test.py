import unittest

from unittest.loader import makeSuite

from test_cases.Filling_the_form_DodajGracza import TestDodajGarczaForm
from test_cases.log_out import TestWyloguj
from test_cases.page_translation import TestTranslations
from test_cases.players_info import TestPlayersPage
from test_cases.framework import Test
from test_cases.click_button_Add_a_player import TestAddPlayer
from test_cases.login_to_the_system import TestLoginPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestAddPlayer))
    test_suite.addTest(makeSuite(TestTranslations))
    test_suite.addTest(makeSuite(TestDodajGarczaForm))
    test_suite.addTest(makeSuite(Test))
    test_suite.addTest(makeSuite(TestWyloguj))
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestPlayersPage))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
