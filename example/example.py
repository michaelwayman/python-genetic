
# Sloppily add genetic classes to our path so we can import it
sys.path.insert(0, os.path.abspath('../genetic'))
from genetic import Evolvable


class EvolvableLineup(Evolvable):
    """
     An example `Evolvable` based on fantasy basketball that is suited for a draftkings basketball lineup.
     """

    @property
    def expected_points(self):
        """The number of draftking points this lineup is expected to produce"""
        if not self.cache_properties:
            self._cache['expected_points'] = sum(
                [player.expected_points for player in self.genes.values() if player])
        return self._cache['expected_points']

    @property
    def cost(self):
        """How much does this lineup cost in terms of salary"""
        if not self.cache_properties:
            self._cache['cost'] = sum(
                [player.salary for player in self.genes.values() if player])
        return self._cache['cost']

    @property
    def unique_str(self):
        if not self.cache_properties:
            players = self.genes.values()
            players.sort(key=lambda k: str(k.name))
            self._cache['unique_str'] = ''.join(str(p.name) for p in players)
        return self._cache['unique_str']

    def can_survive(self):
        """Our lineups cannot survive if they cost more than 50,000"""
        return self.cost <= 50000

    def fitness_level(self):
        """The more draftking points the better the lineup"""
        return self.expected_points

    def unique(self):
        return self.unique_str
