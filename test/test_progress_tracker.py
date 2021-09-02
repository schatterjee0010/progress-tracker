import time
import unittest
from generic_libs import Progress


class TestProgressTracker(unittest.TestCase):
    prg = Progress()

    def setUp(self) -> None:
        pass

    def test_tracker(self):
        func = self.mock_some_wait_func()
        self.assertEqual(func, 2)

    def test_tracker_timeout(self):
        func = self.mock_w_timeout()
        self.assertEqual(func, 2)

    @staticmethod
    @prg.tracker()
    def mock_some_wait_func():
        hit = 1
        time.sleep(10)
        hit += 1
        return hit

    @staticmethod
    @prg.tracker(max_timeout=5)
    def mock_w_timeout():
        hit = 1
        time.sleep(10)
        hit += 1
        return hit
