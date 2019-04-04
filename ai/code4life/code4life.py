import sys

# Bronze League

# Bring data on patient samples from the diagnosis machine to the laboratory with enough molecules to produce medicine!

class Sample():
    def __init__(self, sample_id, carried_by, rank, gain, health, cost):
        self.sample_id = sample_id
        self.carried_by = carried_by
        self.rank = rank
        self.gain = gain
        self.health = health
        self.cost = cost
        self.diagnosed = health != -1

    def __repr__(self):
        return str(self.sample_id)

class Robot():
    def __init__(self, storage, target, expertise):
        self.storage = storage
        self.target = target
        self.expertise = expertise
        self.carrying = []

def goto_and_connect(module, data, position):
    if position == module:
        print("CONNECT " + str(data))
    else:
        print("GOTO " + module)

project_count = int(input())
for i in range(project_count):
    a, b, c, d, e = [int(j) for j in input().split()]

# game loop
while True:
    samples = []
    robots = []

    # robots
    for i in range(2):
        target, eta, score, storage_a, storage_b, storage_c, storage_d, storage_e, expertise_a, expertise_b, expertise_c, expertise_d, expertise_e = input().split()
        eta = int(eta)
        score = int(score)
        storage_a = int(storage_a)
        storage_b = int(storage_b)
        storage_c = int(storage_c)
        storage_d = int(storage_d)
        storage_e = int(storage_e)
        expertise_a = int(expertise_a)
        expertise_b = int(expertise_b)
        expertise_c = int(expertise_c)
        expertise_d = int(expertise_d)
        expertise_e = int(expertise_e)
        storage = [storage_a, storage_b, storage_c, storage_d, storage_e]
        expertise = [expertise_a, expertise_b, expertise_c, expertise_d, expertise_e]
        robot = Robot(storage, target, expertise)
        robots.append(robot)

    available_a, available_b, available_c, available_d, available_e = [int(i) for i in input().split()]

    # samples
    sample_count = int(input())
    for i in range(sample_count):
        sample_id, carried_by, rank, expertise_gain, health, cost_a, cost_b, cost_c, cost_d, cost_e = input().split()
        sample_id = int(sample_id)
        carried_by = int(carried_by)
        rank = int(rank)
        health = int(health)
        cost_a = int(cost_a)
        cost_b = int(cost_b)
        cost_c = int(cost_c)
        cost_d = int(cost_d)
        cost_e = int(cost_e)
        cost = [cost_a, cost_b, cost_c, cost_d, cost_e]
        sample = Sample(sample_id, carried_by, rank, expertise_gain, health, cost)
        samples.append(sample)
        if (carried_by > -1):
            robots[carried_by].carrying.append(sample)

    me = robots[0]

    if (not me.carrying):
        if (sum(me.expertise) < 8):
            goto_and_connect("SAMPLES", 2, me.target)
        else:
            goto_and_connect("SAMPLES", 3, me.target)
    else:
        sample = me.carrying[0]
        if sample.diagnosed:
            needed_molecule = None
            for i in range(5):
                if (me.storage[i] < sample.cost[i] - me.expertise[i]):
                    needed_molecule = "ABCDE"[i]
                    break
            if needed_molecule is not None:
                goto_and_connect("MOLECULES", needed_molecule, me.target)
            else:
                goto_and_connect("LABORATORY", sample.sample_id, me.target)
        else:
            goto_and_connect("DIAGNOSIS", sample.sample_id, me.target)
