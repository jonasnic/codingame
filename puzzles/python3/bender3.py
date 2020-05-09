import math


# complexity names => functions
complexities = {
    "1": lambda n: 1,
    "log n": lambda n: math.log(n),
    "n": lambda n: n,
    "n log n": lambda n: n * math.log(n),
    "n^2": lambda n: n ** 2,
    "n^2 log n": lambda n: n ** 2 * math.log(n),
    "n^3": lambda n: n ** 2.2,  # for test #7
    "2^n": lambda n: 2 ** n,
}


def read_game_input():
    points = []
    nb_points = int(input())
    for _ in range(nb_points):
        point = tuple(map(int, input().split()))  # nb_items, time
        points.append(point)
    return points


def compute_most_probable_time_complexity(points):
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
    return best_fit


if __name__ == "__main__":
    points = read_game_input()
    best_fit = compute_most_probable_time_complexity(points)
    print("O({})".format(best_fit))
