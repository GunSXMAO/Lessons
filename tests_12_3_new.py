from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = Runner("Усэйн", 10)
        self.Andrey = Runner("Андрей", 9)
        self.Nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_usain_nik(self):
        tournament = Tournament(90, self.Usain, self.Nik)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_andrey_nik(self):
        tournament = Tournament(90, self.Andrey, self.Nik)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_usain_andrey_nik(self):
        tournament = Tournament(90, self.Usain, self.Andrey, self.Nik)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()

____________________________________________________________________________________________________________________________________

import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = False
    all_results = {}
    def setUpClass(self):
        self.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner


if __name__ == "__main__":
    unittest.main()

__________________________________________________________________________________________________________________________________________

import unittest
import TournamentTest
import Test_runner


TestSuite = unittest.TestSuite()
TestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))
TestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_runner.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestSuite)

