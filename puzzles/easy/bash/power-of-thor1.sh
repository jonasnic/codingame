# lightX: the X position of the light of power
# lightY: the Y position of the light of power
# x: Thor's starting X position
# y: Thor's starting Y position
read lightX lightY x y

# game loop
while true; do
    # remainingTurns: The remaining amount of turns Thor can move. Do not remove this line.
    read remainingTurns
    move=""

    if ((y > lightY)); then
      move+="N"
      let "y--"
    elif ((y < lightY)); then
      move+="S"
      let "y++"
    fi

    if ((x > lightX)); then
      move+="W"
      let "x--"
    elif ((x < lightX)); then
      move+="E"
      let "x++"
    fi

    # Write an action using echo
    # To debug: echo "Debug messages..." >&2


    # A single line providing the move to be made: N NE E SE S SW W or NW
    echo $move
done
