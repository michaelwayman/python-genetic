# python-genetic

My take on genetic mutation to solve np-complete maximization problems. Originally intended for fantasy sports.

The idea with evolution/genetic algorithms is that you

 1. take a gene pool, and create an initial population from the genes.
 1. select the "most fit" from the population and call them "parents".
 1. breed/combine/cross the parents by exchanging elements between them, usually at random, to create "children", throw in some random genes from the gene pool every so often
 1. take the "most fit" of the children and call them "parents"
 1. go to step 3
 
After many generations of this, the resulting population will typically be pretty "fit"


# Background

I was working on creating an algorithm to try and make $ playing fantasy sports.

After making some predictions about each player's performance, I still needed to combine the individual players to create a team that would perform well.

Initially I tried iterating through every combination of players, but the algorithm was taking a while to complete so I did some math
and realized that there was over 4 quadrillion combinations of players.

After doing some estimations, I realized my algorithm on a single-thread would take days-weeks to complete, unacceptable!!

This new approach with genetic mutation was able to calculate the best combination of players for me in less than a minute :)
