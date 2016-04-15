import unittest
from scorekeeper import *


class TestScorekeeper(unittest.TestCase):

    def test_main_menu_option_1(self):
        self.assertEqual(main_menu("1") == setup())

if __name__ == '__main__':
    unittest.main()
