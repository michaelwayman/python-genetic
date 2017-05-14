import json
import os
import sys


sys.path.insert(0, os.path.abspath('../genetic'))
from evolve import Evolve
from evolvable_nba_team import EvolvableNBATeam


def get_gene_pool():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(file_dir, 'gene_pool.json')
    with open(path) as f:
        return json.loads(f.read())


def print_gene_pool_info(gene_pool):
    number_sequences = reduce(lambda x, y: x * y, map(lambda i: len(i), gene_pool.values()))
    output = (
        '\nGene pool information:\n'
        '  {} Unique Alleles\n'
        '  {} Unique Genes\n'
        '  About {} ({:.2E}) possible DNA sequences\n'
    ).format(
        sum(len(x) for x in gene_pool.values()),
        len(gene_pool),
        number_sequences, number_sequences,
    )
    print(output)


if __name__ == '__main__':

    # Gene Pool
    gene_pool = get_gene_pool()
    print_gene_pool_info(gene_pool)

    # Simulate the natural selection process
    e = Evolve(gene_pool, EvolvableNBATeam)
    e.run(n=50000, n_best=2)

    # Print our final results
    print('\n\nThe {} best DNA sequences after {} generations:\n'.format(2, 50000))
    print('\n\n\n'.join(str(x) for x in e.best))
