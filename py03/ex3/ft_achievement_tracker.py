import random


def gen_player_achievements() -> set:
    achievements = [
        "first_kill", "level_10", "treasure_hunter", 
        "speed_demon", "MVP", "Unstoppable", "boss_slayer",
        "Strategist", "Speed_Runner", "Untouchable", "perfectionist",
        "collector", "Legendary", "Deadeye", "Explorer", "VIP"
        ]
    random_number = random.randint(3, 8)
    player_set = random.sample(achievements, k=random_number)
    return set(player_set)


def uniq_achiev(others: set, plyer: set) -> set:
    lst = list(plyer)
    for l1 in plyer:
        if l1 in others:
            lst.remove(l1)
    return set(lst)


def no_achiev(others: set, plyer: set) -> set:
    lst = list(others)
    for l1 in plyer:
        if l1 in others:
            lst.remove(l1)
    return set(lst)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    # players_list = ["alice", "bob", "charlie", "dylan"]
    # for ply in players_list:
    #     print(f"Player {ply}: {gen_player_achievements()}")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print("Player Alice: ", alice)
    print("Player Bob: ", bob)
    print("Player Charlie: ", charlie)
    print("Player Dylan: ", dylan)
    uni = set.union(dylan, alice, bob, charlie)
#    union = dylan | alice | bob | charlie
    print("\nAll distinct achievements: ", uni)
    inter = set.intersection(dylan, alice, bob, charlie)
#    intersection = alice & bob & charlie & dylan
    print("\nCommon achievements:", inter)
    print("Only Alice has:", uniq_achiev((dylan | bob | charlie), alice))
    print("Only Bob has:", uniq_achiev((dylan | alice | charlie), bob))
    print("Only Charlie has:", uniq_achiev((dylan | bob | alice), charlie))
    print("Only Dylan has:", uniq_achiev((alice | bob | charlie), dylan))
    print("\nAlic is missing:", no_achiev((dylan | bob | charlie), alice))
    print("Bob is missing:", no_achiev((dylan | alice | charlie), bob))
    print("Charlie is missing:", no_achiev((dylan | bob | alice), charlie))
    print("Dylan is missing:", no_achiev((alice | bob | charlie), dylan))


if __name__ == "__main__":
    main()