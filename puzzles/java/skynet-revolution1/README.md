# Skynet Revolution - Episode 1

The objective of this puzzle is to block the path of the Skynet agent to prevent him from reaching an exit.
In order to get the achievement, we can follow a strategy of elimination.
Our first priority is to look for immediate threats (the agent is located right next to an exit).
Our second priority is to attack links to block the agent inside or outside the biggest star pattern.
We find the gateway of the biggest star and then we target links that can block the agent from leaving the star.
Our final priority is to attack the last link on the shortest path between the virus and an exit.
For this we can use <a href="https://en.wikipedia.org/wiki/Breadth-first_search">Breadth First Search</a>.
