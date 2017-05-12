from abc import ABCMeta, abstractmethod


class Evolvable(object):
    """Abstract Base Class to create "evolvable" objects

    Am `Evolvable` represents an object that has "genes".
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
            - please see the code for how to use `_cache` and `cache_properties`
        """
        self._cache = {}
        self.cache_properties = False
        self.genes = {gene: None for gene in genes}

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

    @abstractmethod
    def unique(self):
        """
        Returns:
            some hashable that can uniquely identify the particular sequence of genes (to avoid creating duplicates)
        """
        raise NotImplemented