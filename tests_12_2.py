class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            # В цикле обновляем участников
            for participant in self.participants:
                participant.run()  # Или метод walk(), в зависимости от необходимости
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

________________________________________________________________________________________________

from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
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

    def test_tournament_usain_nik(self):
        tournament = Tournament(90, self.Usain, self.Nik)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

    def test_tournament_andrey_nik(self):
        tournament = Tournament(90, self.Andrey, self.Nik)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

    def test_tournament_usain_andrey_nik(self):
        tournament = Tournament(90, self.Usain, self.Andrey, self.Nik)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()
