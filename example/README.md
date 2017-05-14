#### To run the example

```
python example.py
```


#### Draftkings

In Aug 2016 New York legalized the use of http://draftkings.com, a place where you can gamble on fantasy sports.


#### Fantasy NBA

Let's say we are gambling on the NBA.
The first thing we do is create a "lineup" for today's games.

Draftkings gives us:
 - a list of players that are playing in todays games
 - how much each player costs
 - what positions each player is allowed to play.

A lineup has 8 mandatory positions and we have a budget of $50,000 fantasy dollars.

When a player makes a play in real life, he makes the same play in our fantasy game as well. If a player is injured in real life he also gets injured in our fantasy games.

So each player makes plays, each play earn a certain number "fantasy points", and the lineup with the most fantasy points at the end of the night, wins.


#### The problem

Let's say we know in advance how many fantasy points a player will earn in today's games. That's great, but we still aren't done.
We still need to create our lineups such that we maximize as many fantasy points as possible.

 - We have $50,000 we can spend.
 - 8 positions we need to fill.
 - Each player has a cost and a value (fantasy points).
 - We want to maximize total fantasy points across our lineups.

From our example data there are 4,291,640,676,792,000 (4.29E+15) possible lineups. The goal is to find the best ones.

#### Manual Strategies

A player's cost is typically based on how many fantasy points they are expected to earn.

**Player Costs rule of thumb**
 - Great Players ($11,000-$13,000)
 - Good Players ($8,000-$11,000)
 - Medium Players ($6,000-$8,000)
 - Bad players that will probably play for a quarter ($4,500-$6,000)
 - Bad players that will probably play less than a quarter ($3,000-$4,500)

REMEMBER: your lineup must have exactly 8 players.

**Common lineup strategies**
 - 2 great players, 6 bad players
 - 2 good, 5 medium, 1 bad
 - 1 great, 6 medium, 1 bad
 - 8 medium

Each strategy has its own PROs and CONs, and depending on the type of contest and payout system, might be more or less effective.

#### The solution

Iterating through every possible lineup and combination of players would take days, possibly even months. The Genetic mutation algorithm can find the maximum lineups in less than a minute. The tradeoff, like all heuristic algorithms, is that there is no guarantee the answer is 100% accurate.
