import unittest
import time
from StopwatchClass import Stopwatch


class TestStopwatch(unittest.TestCase):

    def test_start_stop(self):
        stopwatch = Stopwatch()
        self.assertFalse(stopwatch.is_running)
        stopwatch.start()
        self.assertTrue(stopwatch.is_running)
        time.sleep(0.1)
        stopwatch.stop()
        self.assertFalse(stopwatch.is_running)
        elapsed_millisecond = stopwatch.elapsed_milliseconds
        self.assertGreaterEqual(elapsed_millisecond, 100)
        time.sleep(0.1)
        self.assertEqual(elapsed_millisecond, stopwatch.elapsed_milliseconds)

    def test_start_stop_resume(self):
        stopwatch = Stopwatch()
        stopwatch.start()
        time.sleep(0.1)
        stopwatch.stop()
        stopwatch.start()
        time.sleep(0.1)
        self.assertGreaterEqual(stopwatch.elapsed_milliseconds, 200)

    def test_start_stop_reset(self):
        stopwatch = Stopwatch()
        self.assertEqual(stopwatch.elapsed_milliseconds, 0)
        stopwatch.start()
        time.sleep(0.1)
        stopwatch.stop()
        stopwatch.reset()
        self.assertEqual(stopwatch.elapsed_milliseconds, 0)

    def test_start_restart(self):
        stopwatch = Stopwatch()
        stopwatch.start()
        time.sleep(0.5)
        stopwatch.restart()
        self.assertLess(stopwatch.elapsed_milliseconds, 500)
        time.sleep(0.1)
        self.assertGreaterEqual(stopwatch.elapsed_milliseconds, 100)

    def test_start_new(self):
        stopwatch = Stopwatch.start_new()
        self.assertTrue(stopwatch.is_running)
        time.sleep(0.1)
        stopwatch.stop()
        self.assertFalse(stopwatch.is_running)
        self.assertGreaterEqual(stopwatch.elapsed_milliseconds, 100)


if __name__ == '__main__':
    unittest.main()
