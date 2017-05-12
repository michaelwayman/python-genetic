
> In computer science, a genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover and selection.

This is *my* take of a genetic mutation algorithm I had to come up with to solve a real world 4x10^15 choices *np-complete* maximization problem.

The the algorithm is pretty straitforward with a couple caveats, but first let's understand the 2 classes.

### Evolvables

`class Evolvable:` - AbstractBaseClass that represents: something that can "evolve", or a particular state/solution to a problem

An evolvable has 4 pieces of information:
 1. `genes` which is our solution representation
 2. `can_survive` a True/False value of this evolvable is a valid solution or not
 3. `fitness_level` a number that tells us how good of a solution this is
 4. `unique` some hashable representation to uniquely identify this solution (maybe a serialization of the genes?) it could be anything

### Evolve

`class Evolve:` - Class that takes some kind of Evolvable and simulates the "natural selection" process creating countless generations of evolvable instances. The goal is that over enough generations of natural selection, that the final solutions/evolvables are the right ones.

The important pieces of the Evolve class:
 - `gene_pool` all the different genes that we can use when creating Evolvable instances.
 - `best` this is a list of the best Evolvables throughout the generations
 - `population` the current generation of evolvables
 - `cross_over` a function that takes 2 or more evolvable instances (parents) and creates new evolvables from them (children).
 - `mutate` a function that takes an evolvable and introduces switches 1 or more of the evolvable's genes with genes from the gene pool.

___

### Chess Example

We could represent the next move in a game of chess as an Evolvable:
 1. the arrangement of pieces would be the `genes`
 2. `can_survive` - if the next move is valid or not
 3. `fitness_level` 1.0 if we get them in checkmate, 0.3 if we lose position, 0.0 if we move our queen into danger for no reason
 4. `unique` could be the arrangement of pieces

This is just a way to represent 1 potential move in a game of chess as an Evolvable, but if we think about it, we could actually represent an entire game as a series of Evolvables. One evolvable (move) giving rise to the next move (evolvable) and so on, until eventually the game is over.

___

#### Background

I had a notion that I could make a lot of *$$ money $$* by creating an algorithm that could win at fantasy sports (online fantasy sport gambling was just made legal in NY, I was pretty excited)

After making individual player predictions, I needed to form full teams from the players.

Depending on the night, there could be up to 4 quadrillion (4x10^15) possible combinations of teams.

After doing some estimations, looking at all these combinations would take days-weeks to complete, unacceptable!!

I came up with this genetic mutation algorithm and was able to calculate the best combination of players in less than a minute :)
