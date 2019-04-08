#!/bin/bash
ok=0
total=0
file="tests.txt"
printf "\n***** $file *****\n"
while IFS=: read -r name
do
  let "total += 1"
  printf "test $name\n"
  fileName="$name.txt"
  eval "python3 tan_network.py < "test/$fileName" &> act.txt"

  diff --text "exp/$fileName" "act.txt"
  if [ $? != 0 ]; then
    printf "test $total FAILED\n"
    printf 'name: %s\n' "$args"
  else
    let "ok += 1"
  fi
done <"$file"

printf "\npasses $ok out of $total tests\n"
