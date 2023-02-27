#Faceti o suita care sa contina testele voastre de la tema 9 + testele de la
#intalnirea 10 (care au clasa). Generati raportul

'''
Ganditi voi o clasa de test din paginile sugerate in tema 8
- Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi firefox in loc de chrome (ce doriti voi, cate functii de test doriti,
freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test).
'''

import unittest
import HtmlTestRunner

from Teme_programare.tema_9 import Login
from Curs_programare.curs_10.auth import Authentication
from Curs_programare.curs_10.allerts import Alerts
from Curs_programare.curs_10.context_menu import ContextMenu
from Curs_programare.curs_10.key_press import Keyboard
from Curs_programare.curs_10.suites import TestSuite

class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_to_run = unittest.TestSuite()
        test_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSuite)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='My Report Name',
            report_title='My First Report Title'
        )

        runner.run(test_to_run)