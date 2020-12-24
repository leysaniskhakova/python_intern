
import unittest

from app import is_alive_host


class TestApp1(unittest.TestCase):

    def test_alive_host(self):
        self.assertEqual(is_alive_host('ya.ru'), {'status': 'up'})


    def test_down_host(self):
        self.assertEqual(is_alive_host('sdkfjs.ru'), {'status': 'down'})

if __name__ == '__main__':
    unittest.main()