import json
import os
import sys


sys.path.insert(0, os.path.abspath('../genetic'))
from evolve import Evolve
from evolvable_nba_team import EvolvableNBATeam


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_gene_pool():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(file_dir, 'gene_pool.json')

    with open(path) as f:
        return json.loads(f.read())


def print_gene_pool_info(gene_pool):
    number_sequences = reduce(lambda x, y: x * y, map(lambda i: len(i), gene_pool.values()))
    output = (
        '\n{}Gene pool information:{}\n'
        '  {}{}{} {}Unique Alleles{}\n'
        '  {}{}{} {}Unique Genes{}\n'
        '  About {}{}{} ({:.2E}) possible DNA sequences\n'
    ).format(
        Colors.UNDERLINE, Colors.ENDC,
        Colors.BOLD, sum(len(x) for x in gene_pool.values()), Colors.ENDC, Colors.OKBLUE, Colors.ENDC,
        Colors.BOLD, len(gene_pool), Colors.ENDC, Colors.OKGREEN, Colors.ENDC,
        Colors.HEADER, number_sequences, Colors.ENDC, number_sequences,
    )
    print(output)


if __name__ == '__main__':
    gene_pool = get_gene_pool()
    print_gene_pool_info(gene_pool)

    n_generations = 50000
    n_best = 2

    e = Evolve(gene_pool, EvolvableNBATeam)
    e.run(n=n_generations, n_best=n_best)

    print('\n\nThe {} best DNA sequences after {} generations:\n'.format(n_best, n_generations))
    print(e)
