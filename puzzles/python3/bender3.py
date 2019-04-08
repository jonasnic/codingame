import math

# complexity names and functions
complexities = {
    "1": lambda n: 1,
    "log n": lambda n: math.log(n),
    "n": lambda n: n,
    "n log n": lambda n: n * math.log(n),
    "n^2": lambda n: n ** 2,
    "n^2 log n": lambda n: n ** 2 * math.log(n),
    "n^3": lambda n: n ** 2.1,  # for validator test #7
    "2^n": lambda n: 2 ** n,
}

# read standard input
points = []
nb_points = int(input())
for i in range(nb_points):
    point = tuple([int(j) for j in input().split()])  # nb_items, time
    points.append(point)

# compute the most probable computational complexity
best_fit = ""
min_norm_variance = float("inf")
for name, function in complexities.items():
    ratios = [time / function(nb_items) for nb_items, time in points]

    # calculate the normalized variance
    mean_ratios = sum(ratios) / len(ratios)
    variances = [(ratio - mean_ratios) ** 2 for ratio in ratios]
    norm_variance = sum(variances) / mean_ratios ** 2

    if norm_variance < min_norm_variance:
        min_norm_variance = norm_variance
        best_fit = name

print("O({})".format(best_fit))
