#### To run the example

```
python example.py
```


#### Draftkings

In Aug 2016 New York legalized the use of http://draftkings.com, a place where you can gamble on fantasy sports.
Creating an algorithm that can win at fantasy sports could win you a lot of money.


#### Fantasy NBA

Let's say we are gambling in daily fantasy NBA.
The first thing we do is create a "lineup" for today's games.

Draftkings gives us:
 - a list of players that are playing in todays games
 - how much each player costs
 - what positions each player is allowed to play.

A lineup has 8 mandatory positions and we have a budget of $50,000 fantasy dollars that we can use to buy players for our lineups.

When a player scores a basket in real life, he scores a basket in fantasy as well. The same applies for fouls, turnovers, steals, blocks, assists, etc. If a player is injured in real life he gets injured in our fantasy games as well.

So each player is going to earn a certain number of "fantasy points", and the lineup with the most fantasy points wins.


#### The problem

Let's say we can see into the future and we know exactly how many fantasy points a player will get. That's great, but we still aren't done, we've only solved 1/2 the problem. We still need to create our lineups from the individual players so that we maximize as many fantasy points as possible.

 - We have $50,000 we can spend.
 - 8 positions we **have** to fill and a bunch of players to choose from.
 - Each player scores a certain number of fantasy points.
 - We want to maximize total fantasy points across our lineups.

From our example data there are 4,291,640,676,792,000 (4.29E+15) possible lineups. The goal is to find the best ones.


#### The solution

Iterating through every lineup trying to find the maximum takes days, if not, longer. The Genetic mutation algorithm can find the maximum lineups in less than a minute. The tradeoff, of course, is that there is no guarantee the answer is 100% accurate.

Caveats:
 - There is no "stopping" point, the natural selection process will continue indeffinitely, so we usually do this by stopping after `n` generations.
 - If the `gene_pool` isn't big enough, it's possible to run into an infinite loop during natural selection.

