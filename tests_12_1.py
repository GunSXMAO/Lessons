from runner import Runner
import unittest

class TestRunner(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Runner 1")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Runner 2")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1, runner2)

if __name__ == "__main__":
    unittest.main()