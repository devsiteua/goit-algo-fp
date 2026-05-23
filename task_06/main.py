items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )

    selected_items = []
    total_cost = 0

    for name, values in sorted_items:
        if total_cost + values["cost"] <= budget:
            selected_items.append(name)
            total_cost += values["cost"]

    return selected_items


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    table = [[0] * (budget + 1) for _ in range(len(item_names) + 1)]

    for i in range(1, len(item_names) + 1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]["cost"]
        item_calories = items[item_name]["calories"]

        for current_budget in range(budget + 1):
            if item_cost > current_budget:
                table[i][current_budget] = table[i - 1][current_budget]
            else:
                without_item = table[i - 1][current_budget]
                with_item = table[i - 1][current_budget - item_cost] + item_calories
                table[i][current_budget] = max(without_item, with_item)

    selected_items = []
    current_budget = budget

    for i in range(len(item_names), 0, -1):
        if table[i][current_budget] != table[i - 1][current_budget]:
            item_name = item_names[i - 1]
            selected_items.append(item_name)
            current_budget -= items[item_name]["cost"]

    selected_items.reverse()
    return selected_items


def calculate_totals(items, selected_items):
    total_cost = 0
    total_calories = 0

    for item_name in selected_items:
        total_cost += items[item_name]["cost"]
        total_calories += items[item_name]["calories"]

    return total_cost, total_calories


def print_result(title, items, selected_items):
    total_cost, total_calories = calculate_totals(items, selected_items)

    print(title)
    print(f"Selected items: {', '.join(selected_items)}")
    print(f"Total cost: {total_cost}")
    print(f"Total calories: {total_calories}")


def run_tests():
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    greedy_cost, greedy_calories = calculate_totals(items, greedy_result)

    assert greedy_result == ["cola", "potato", "pepsi", "hot-dog"]
    assert greedy_cost <= budget
    assert greedy_calories == 870

    dp_result = dynamic_programming(items, budget)
    dp_cost, dp_calories = calculate_totals(items, dp_result)

    assert dp_result == ["pizza", "pepsi", "cola", "potato"]
    assert dp_cost <= budget
    assert dp_calories == 970

    assert greedy_algorithm(items, 0) == []
    assert dynamic_programming(items, 0) == []


def main():
    run_tests()

    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print(f"Budget: {budget}\n")
    print_result("Greedy algorithm result:", items, greedy_result)
    print()
    print_result("Dynamic programming result:", items, dp_result)


if __name__ == "__main__":
    main()
