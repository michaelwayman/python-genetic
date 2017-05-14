from abc import ABCMeta, abstractmethod


class Evolvable(object):
    """Abstract Base Class to create "evolvable" objects

    An `Evolvable` represents an object that has a specific set of "genes" and "alleles".
    A "gene" represents a broader idea, like "hair color", whereas an "allele" is a particular
    mutation of the hair color gene, giving us: blondes, brunettes, etc.

    An `Evolvable`s value to us, is that in its complete state, represents a solution to a particular problem.

    The idea of the Evolvable class is that multiple instances
    can be combined to create new Evolvables.
    """
    __metaclass__ = ABCMeta

    def __init__(self, genes):
        """
        Args:
            genes: list of the genes that each `Evolvable` must have

        Note:
            - Subclasses of this ABC should call super on this method.
            - `_cache` and `cache_attrs` are for performance optimizations.
        """
        self.genes = {gene: None for gene in genes}

        # Once an instance of `Evolvable` is complete and not going to change, the `Evolve` class
        # will set `cache_attrs` to True. We can make use of this for better performance.
        self.cache_attrs = False
        self._cache = {}

    @abstractmethod
    def can_survive(self):
        """
        Returns:
             A boolean whether or not this `Evolvable`
             can survive in the wild.
             """
        raise NotImplemented

    @abstractmethod
    def fitness_level(self):
        """
        Returns:
            some sort of number that summarizes how desirable this `Evolvable`
            genes are. (The bigger the better)
        """
        raise NotImplemented

    def unique(self):
        """
        Note:
            Depending on what your genes look like you might want override this method for something more efficient

        Returns:
            some hashable that can uniquely identify the particular sequence of genes (to avoid creating duplicates)
        """
        if self.cache_attrs:
            if 'unique' not in self._cache:
                self._cache['unique'] = str(sorted(self.genes.items()))
            return self._cache['unique']
        return str(sorted(self.genes.items()))
