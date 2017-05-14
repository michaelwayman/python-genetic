import os
import sys

# Sloppily add genetic classes to our path so we can import it
sys.path.insert(0, os.path.abspath('../genetic'))
from evolvable import Evolvable


class EvolvableNBATeam(Evolvable):
    """
     An example `Evolvable` based on fantasy basketball that is suited for a draftkings basketball lineup.
     """

    @property
    def expected_points(self):
        """ The number of draftking points this lineup is expected to produce. """
        if self.cache_attrs:
            if 'expected_points' not in self._cache:
                self._cache['expected_points'] = sum([player['average_points'] for player in self.genes.values() if player])
            return self._cache['expected_points']
        return sum([player['average_points'] for player in self.genes.values() if player])

    @property
    def cost(self):
        """ How much does this lineup cost in terms of salary. """
        if self.cache_attrs:
            if 'cost' not in self._cache:
                self._cache['cost'] = sum([player['cost'] for player in self.genes.values() if player])
            return self._cache['cost']
        return sum([player['cost'] for player in self.genes.values() if player])

    def can_survive(self):
        """ Our lineups cannot survive if they cost more than 50,000 """
        return self.cost <= 50000

    def fitness_level(self):
        """ The more draftking points the better the lineup """
        return self.expected_points

    def __str__(self):
        """
        Please ignore this function.
        I'm going to trade pretty code for pretty output.
        """
        border = '=' * 90

        def table_format(columns):
            cols = {0: 10, 1: 30, 2: 10, 3: 10}
            out = []
            for i, col in enumerate(columns):
                col = str(col)
                o = '    ' + col + (' ' * (cols[i] - len(col)))
                out.append(o)
            return ' | '.join(out)

        output = []

        # Add our table headers
        output.extend([border, table_format(('Gene', 'Allele', '', 'Fitness Level')), border])

        # Add our table body
        for g, p in self.genes.items():
            output.append(table_format((g, p['name'], p['cost'], round(p['average_points'], 2))))

        # Add our table footer
        output.extend([border, table_format(('total', '', self.cost, round(self.expected_points, 2))), border])

        return '\n'.join(output)
