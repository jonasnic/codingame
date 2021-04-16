import sys
import math


def debug(*x): print(*x, file=sys.stderr, flush=True)


def ClosestStack(x):  # does not work.....
    potensial = {}
    for i, stack in enumerate(stacks):
        if stack[-1] == x:
            return i  # simple, if the letter match just return this index

        diffrence = ord(x)-ord(stack[-1])
        if diffrence < 0:
            potensial[diffrence] = i

    return potensial[max(potensial)]  # index of stack with closest match with letters above it


n = int(input())
for i in range(n):
    line = input()  # truck line
    stacks = ["Ø" for i in range(len(line))]  # just prepare a long list
    # debug(stacks)

    for container in line:
        bestStack = ClosestStack(container)
        stacks[bestStack] += container  # add container to this stack
        # debug(stacks)

    r = []
    for i in stacks:
        if len(i) > 1:
            r.append(i)
            debug("", i)
    debug(line)
    print(len(r))
