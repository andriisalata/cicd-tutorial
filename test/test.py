import unittest
import pytest
from app.main import hello_world


class TestHelloWorld(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_simple(self):
        expected_output = "Hello World!\n"
        hello_world()
        captured = self.capsys.readouterr()
        self.assertEqual(captured.out, expected_output)

