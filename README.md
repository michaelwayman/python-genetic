
> In computer science, a genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover and selection.

This is *my* take on natural selection and genetic mutation. Original content here, you won't find this anywhere else. In the [example](https://github.com/michaelwayman/python-genetic/tree/master/example) you can see it solve a real world 4.29x10^15 choices *np-complete* maximization problem.

This may sound like a boring problem but for real check out the [example](https://github.com/michaelwayman/python-genetic/tree/master/example) and read the problem description. It's based on real-world basketball data to solve a hardcore maximization problem.

## Usage

3 easy steps:
 1. subclass `Evolvable` to model your problem
 2. create your `gene_pool`
 3. perform the natural selection for n number of generations

#### First

Subclass `Evolvable` in a way that represents the problem you are trying to solve. Don't worry, there are only 3 simple functions you need to implement.

```python
class MyEvolvable(Evolvable):

    def can_survive(self):
        return len(self.genes > 64)

    def fitness_level(self):
        return map_genes_to_values(self.genes)

    def unique(self):
        return str(self.genes)
```

#### Second

Create a gene_pool that maps all your genes to their corresponding alleles.
Remember, a Gene is just an idea of something, like 'hair color'. Whereas 'alleles' are the actual mutation/expression of a gene like 'blonde' or 'brunette'

```python
gene_pool = {
    'hair_color': ['blonde', 'brunette', 'black'],
    'height': ['short', 'tall', 'fun-size'],
    'weight': ['skinny', 'normal', 'overweight'],
    ...
}
```

#### Third

Perform the natural selection on your Evolvable using your gene_pool.

```python
e = Evolve(gene_pool, MyEvolvable)
e.run(n=75000)

# 75,000 generations later, e will have our best answers.
print(e)
```

### Evolvables

`class Evolvable:` - represents 2 things: something that can "evolve", and a solution to a particular problem

An evolvable has 4 pieces of information:
 1. `genes` representation of the solution
 2. `can_survive` something to tell us if this is a valid solution or not
 3. `fitness_level` a number that tells us how good of a solution this is
 4. `unique` some hashable representation to uniquely identify this solution (maybe a serialization of the genes?) it could be anything

### Evolve

`class Evolve:` - Class that takes a type of Evolvable and simulates the "natural selection" process.

The important pieces of the Evolve class:
 - `gene_pool` all the different genes and alleles available to create Evolvable instances with.
 - `best` list of the best Evolvables throughout the generations
 - `population` the current generation of evolvables
 - `cross_over` a function that takes 2 or more evolvable instances (parents) and creates new evolvables from them (children).
 - `mutate` a function that takes an evolvable and switches a couple of the alleles with alleles from the gene pool.

#### Background

I had a notion that I could make a lot of *$$ money $$* by creating an algorithm that could win at fantasy sports (gambling on fantasy sports was just made legal in NY, I was pretty excited)

Depending on the night, there could be up to 4.5 quadrillion (4.5x10^15) possible combinations of teams.

After doing some estimations, looking at all these combinations would take days to weeks to complete.

I came up with this genetic mutation algorithm and was able to calculate the best combination of players in less than a minute :)
