# The Descent

The goal here is to prevent our ship from crashing into mountains.
In order to suceed, our ship must shoot the tallest mountain on each turn.
Therefore, we use the variable `max` to track the max height and also `indexMax` for the index to shoot.
On every turn, all mountain heights are read from the standard input.
We update our variables when a new max is found.
Finally, we print `indexMax` to the standard output.
