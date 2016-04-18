from unittest import TestCase
from games import app


class AppTest(TestCase):

    def setUp(self):
        self.cls = app.App()

    def test_array(self):
        self.assertRaises(NotImplementedError, self.cls.array())

    def test_control(self):
        self.assertRaises(NotImplementedError, self.cls.control(None))

    def test_print_board(self):
        pass

    def test_end_game(self):
        self.assertRaises(app.Stop, self.cls.end_game(0))
        self.assertRaises(app.Stop, self.cls.end_game(1))
