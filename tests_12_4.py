from rt_with_exceptions import Runner, Tournament
import unittest
import logging

class TestRunner(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')
        logging.info("Начало выполнения тестов класса TestRunner")

    def tearDown(self):
        logging.info(f"Завершение теста: {self.id()}")

    def test_walk(self):
        try:
            logging.info('Начало выполнения теста test_walk')
            runner = Runner('runner1', speed = -20)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner', exc_info=True)
            self.fail("Не удалось пройти тест test_walk")

    def test_run(self):
        try:
            logging.info('Начало выполнения теста test_run')
            runner = Runner(123)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
            self.fail("Не удалось пройти тест test_run")

    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1, runner2)

if __name__ == "__main__":
    unittest.main()
