import random


class Evolve(object):
    """Evolve takes a `gene_pool` and an `Evolvable` type, and simulates natural selection.

    Capable of solving very complex np-complete optimization problems in a couple minutes that
    would otherwise take days or weeks or months to solve.
    """

    def __init__(self, gene_pool, evolvable_class):
        """
        Args:
            gene_pool: A dictionary with "genes" for keys, and a list of "alleles" as the value.
            evolvable_class: The type of evolvables we are going to evolve

        Note:
            `self.best` an aggregate of the best `Evolvable`s from every generation
            `self.population` represents the *current* population
        """
        self.gene_pool = gene_pool
        self.population = []
        self.best = []
        self.evolvable_class = evolvable_class

    def run(self, n=1000, n_best=5, n_children=4):
        """Starts and runs the natural selection process.

        1. Create the initial population
        2. Select the 'most fit' from the population and "breed" them, creating the next generation
        3. Repeat #2 `n` times.

        Args:
            n: the number of generations
            n_best: keep track of the n_best evolvables of all time
            n_children: the number of children each group of parents should produce
        """
        if not self.population:
            self.population = [self.generate_random_parent() for _ in range(n_children)]
            self.set_best()

        for i in xrange(n):
            parents = self.best_parents()
            self.population = [self.cross_over(parents) for _ in range(n_children)]
            self.set_best(n_best=n_best)

    def set_best(self, n_best=5):
        """
        Updates the "best of all time" (if needed).
        """
        unique = set()
        values = self.best + self.population
        best = []
        for v in values:
            if v.unique() not in unique:
                unique.add(v.unique())
                best.append(v)
        self.best = sorted(
            best,
            key=lambda k: k.fitness_level(), reverse=True)[:n_best]

    def best_parents(self, n=2):
        """Select the best n `Evolvable`s from the current population.

        Args:
            n: # of best parents to return

        Returns:
            List of the best `Evolvable`s from the current population.
        """
        return sorted(self.population, key=lambda k: k.fitness_level(), reverse=True)[:n]

    def generate_random_parent(self):
        """Generates a random `Evolvable` using genes from the `gene_pool`.

        Returns:
            Evolvable randomly created from the `gene_pool`
        """
        parent = self.evolvable_class(self.gene_pool.keys())
        while True:
            for gene, allele in self.gene_pool.iteritems():
                while True:
                    random_allele = random.choice(allele)
                    if random_allele not in parent.genes.values():
                        parent.genes[gene] = random_allele
                        break
            if parent.can_survive():
                parent.cache = True
                return parent

    def cross_over(self, parents):
        """Combines 1 or more parents into a single child.

        For each gene in the child this function will choose the allele from a random parent
        If no allele from a parent "fits" the child, then use an allele from the 'gene_pool'

        Args:
            parents (Evolvable): sequence of `Evolvable`s

        Note:
            If no alleles from the `gene_pool` are used then we call `mutate()`on the child.

        Returns:
            Evolvable created by combining the parents and inserting a random mutation from the `gene_pool`.
        """
        child = self.evolvable_class(self.gene_pool.keys())

        while True:
            mutated = False

            for gene in self.gene_pool.keys():
                random_parent = random.choice(parents)
                random_allele = random_parent.genes[gene]

                while True:
                    if random_allele not in child.genes.values():
                        child.genes[gene] = random_allele
                        break
                    mutated = True
                    random_allele = random.choice(self.gene_pool[gene])
            if not mutated:
                self.mutate(child)

            if child.can_survive():
                child.cache = True
                return child

    def mutate(self, evolvable, n1=1, n2=2):
        """
        Takes an Evolvable and randomly replaces between n1-n2 of its genes from the gene pool.
        Args:
            evolvable: The Evolvable to mutate
            n1: minimum # of genes to replace
            n2: maximum # of genes to replace

        Returns:
            None
        """
        swap = random.randint(n1, n2)
        for i in range(swap):
            while True:
                random_gene = random.choice(self.gene_pool.keys())
                random_allele = random.choice(self.gene_pool[random_gene])
                if random_allele not in evolvable.genes.values():
                    evolvable.genes[random_gene] = random_allele
                    break

    def __str__(self):
        return '\n\n'.join(str(x) for x in self.best)
