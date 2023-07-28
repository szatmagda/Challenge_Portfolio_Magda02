import unittest

from unittest.loader import makeSuite

from test_cases.Dev_Team_Contact_button import TestDevTeamContact
from test_cases.Filling_the_form_DodajGracza import TestDodajGarczaForm
from test_cases.Log_out import TestWyloguj
from test_cases.Players_info import TestEditForm, TestMeczeButton
from test_cases.framework import Test
from test_cases.Click_button_Add_a_player import TestAddPlayer
from test_cases.login_to_the_system import TestLoginPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestAddPlayer))
    test_suite.addTest(makeSuite(TestDevTeamContact))
    test_suite.addTest(makeSuite(TestDodajGarczaForm))
    test_suite.addTest(makeSuite(Test))
    test_suite.addTest(makeSuite(TestWyloguj))
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestEditForm))
    test_suite.addTest(makeSuite(TestMeczeButton))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())