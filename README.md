
## Genetic Mutation

How to use the process of evolution and natural selection to solve problems.

What you will find here is original content, *my* take on natural selection and genetic mutation that you won't find anywhere else. In the [example](https://github.com/michaelwayman/python-genetic/tree/master/example) you can see it solve a real world 4.29x10^15 choices *np-complete* maximization problem.

> In computer science, a genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover and selection.
> -- <cite>Wikipedia</cite>

## Usage

3 easy steps:
 1. subclass `Evolvable` to model your problem
 2. create your `gene_pool`
 3. Use the `Evolve` class to simulate the evolution and natural selection over `n` number of generations.

#### First

Subclass `Evolvable` in a way that models the problem you are trying to solve. There are only 2 simple functions you need to implement.

```python
class MyEvolvable(Evolvable):

    def can_survive(self):
        # TODO: Return a boolean

    def fitness_level(self):
        # TODO: Return a number (bigger means better)
```

#### Second

Create a gene_pool that maps all your genes to their corresponding alleles.
For the sake of simplicity, a Gene is just an idea, like 'hair color'. Whereas, 'alleles', are the actual mutation/implementation of a gene.

For example,

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

# 75,000 generations later, e.best will have our best answers.
print(str(x) for x in e.best))
```


## The classes

There are only 2 classes that you need to familiarize yourself with to make GA/EA algorithms work.

#### Evolvables

`class Evolvable:` - represents 2 things: something that can "evolve", and a solution to a particular problem

An evolvable has a few pieces of information:
 - `genes` representation of the solution
 - `can_survive` something to tell us if this is a valid solution or not
 - `fitness_level` a number that tells us how good of a solution this is
 - `unique` some hashable representation to uniquely identify this solution (maybe a serialization of the genes?) it could be anything

#### Evolve

`class Evolve:` - Class that takes a type of Evolvable and simulates the "natural selection" process.

The important pieces of the Evolve class:
 - `gene_pool` all the different genes and alleles available to create Evolvable instances with.
 - `best` list of the best Evolvables throughout the generations
 - `population` the current generation of evolvables
 - `cross_over` a function that takes 2 or more evolvable instances (parents) and creates new evolvables from them (children).
 - `mutate` a function that takes an evolvable and switches a couple of the alleles with alleles from the gene pool.

## Background

I had a notion that I could make a lot of *$$ money $$* by creating an algorithm that could win at fantasy sports (gambling on fantasy sports was just made legal in NY, I was pretty excited)

Depending on the night, there could be up to 4.5 quadrillion (4.5x10^15) possible combinations of teams.

After doing some estimations, looking at all these combinations would take days to weeks to complete.

I came up with this genetic mutation algorithm and was able to calculate the best combination of players in less than a minute :)


## Gotchas

 - There is no big-Oh notation or `O(n^2)` way of describing the performance of this algorithm
     + In fact, we actually give the algorithm a stopping point ourselves by saying "evolve 50,000,000 generations and then quit"
 - If the `gene_pool` isn't big enough, it's possible to run into an infinite loop during natural selection.
     + Basically, if we are unable to create `n_children` unique children from the `gene_pool`, we will run into an infinite loop. It would be easy to throw an error in such situations, but really, just make sure your `gene_pool` is large enough to create a large population.
 - There is no guarantee that the next generation will be better than the previous. It is very possible to evolve from something terrible, to something great, back to something terrible. This is why it is important to keep track of the best Evolvables throughout the generations.
 - It's possible to never come across the correct answer. There is so much randomness involved in this algorithm that sometimes it feels like we are just picking a random answer. But the results speak for themselves and it turns out this actually works, quite well.