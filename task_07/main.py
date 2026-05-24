import random


ANALYTICAL_COUNTS = {
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1,
}


def roll_dice():
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)

    return first_dice + second_dice


def monte_carlo_simulation(number_of_rolls):
    results = {}

    for dice_sum in range(2, 13):
        results[dice_sum] = 0

    for _ in range(number_of_rolls):
        dice_sum = roll_dice()
        results[dice_sum] += 1

    return results


def calculate_probabilities(results, number_of_rolls):
    probabilities = {}

    for dice_sum, count in results.items():
        probabilities[dice_sum] = count / number_of_rolls * 100

    return probabilities


def get_analytical_probabilities():
    probabilities = {}

    for dice_sum, count in ANALYTICAL_COUNTS.items():
        probabilities[dice_sum] = count / 36 * 100

    return probabilities


def print_table(monte_carlo_probabilities, analytical_probabilities):
    print("Sum | Monte Carlo | Analytical | Difference")
    print("----|-------------|------------|-----------")

    for dice_sum in range(2, 13):
        monte_carlo_value = monte_carlo_probabilities[dice_sum]
        analytical_value = analytical_probabilities[dice_sum]
        difference = abs(monte_carlo_value - analytical_value)

        print(
            f"{dice_sum:>3} | "
            f"{monte_carlo_value:>10.2f}% | "
            f"{analytical_value:>9.2f}% | "
            f"{difference:>8.2f}%"
        )


def run_tests():
    analytical_probabilities = get_analytical_probabilities()
    total_probability = sum(analytical_probabilities.values())

    assert round(total_probability, 2) == 100.00
    assert ANALYTICAL_COUNTS[2] == 1
    assert ANALYTICAL_COUNTS[7] == 6
    assert ANALYTICAL_COUNTS[12] == 1

    random.seed(1)
    results = monte_carlo_simulation(1000)

    assert sum(results.values()) == 1000
    assert set(results.keys()) == set(range(2, 13))


def main():
    run_tests()

    number_of_rolls = 100000
    random.seed(42)

    results = monte_carlo_simulation(number_of_rolls)
    monte_carlo_probabilities = calculate_probabilities(results, number_of_rolls)
    analytical_probabilities = get_analytical_probabilities()

    print(f"Number of rolls: {number_of_rolls}\n")
    print_table(monte_carlo_probabilities, analytical_probabilities)


if __name__ == "__main__":
    main()
