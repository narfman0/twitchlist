import unittest
from twitchlist import main


class TestMain(unittest.TestCase):
    def test_p(self):
        main.p("test")
