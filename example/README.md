I still need to copy some player data in here to get the example to a point where it is working out-of-the-box.

### How it works with fantasy basketball

###### Terminology In Basketball

 - Gene Pool - all the NBA Players
 - Entity/Child/Parent - a team of NBA players
 - Population - all the teams in the NBA
 - Cross/Breed/Combine - when 2 or more teams in the NBA trade players

###### The algorithm (high level) In Basketball

 1. Create a few teams by randomly selecting players. Careful though, we still need a players to play the right positions, like a guard still needs to play a guard on the team you create, but choose a random guard.
 1. Out of the teams that you randomly created, pick the ones you think will do the best. You can come up with these metrics yourself. E.g. best 3pt%, most assists, etc. It's up to you, just make it realistic.
 1. Once you have the best teams, you want to cross them. Take the best players from each team and combine them into a "super team". Every now and then randomly bring in a player from some other teams, or a rookie you think will take off.
 1. Once you have these new "super teams" go back to step 2. and choose the best of the best from the super teams.

After doing this process many times, the final teams will typically be the best.
