import random


def gen_player_achievements() -> set:
    achievements = [
        "first_kill", "level_10", "treasure_hunter", 
        "speed_demon", "MVP", "Unstoppable", "boss_slayer",
        "Strategist", "Speed_Runner", "Untouchable", "perfectionist",
        "collector", "Legendary", "Deadeye", "Explorer", "VIP"
        ]
    random_number = random.randint(3, 8)
    return set(random.sample(achievements, random_number))


# def uniq_achiev(others: set, plyer: set) -> set:
#     lst = list(plyer)
#     for l1 in plyer:
#         if l1 in others:
#             lst.remove(l1)
#     return set(lst)


# def no_achiev(others: set, plyer: set) -> set:
#     lst = list(others)
#     for l1 in plyer:
#         if l1 in others:
#             lst.remove(l1)
#     return set(lst)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print("Player Alice: ", alice)
    print("Player Bob: ", bob)
    print("Player Charlie: ", charlie)
    print("Player Dylan: ", dylan)
    ach_distinct = set.union(dylan, alice, bob, charlie)
#    union = dylan | alice | bob | charlie
    print("\nAll distinct achievements: ", ach_distinct)
    common = set.intersection(dylan, alice, bob, charlie)
#    intersection = alice & bob & charlie & dylan
    print("\nCommon achievements:", common)
    # print("Only Alice has:", uniq_achiev((dylan | bob | charlie), alice))
    # print("Only Bob has:", uniq_achiev((dylan | alice | charlie), bob))
    # print("Only Charlie has:", uniq_achiev((dylan | bob | alice), charlie))
    # print("Only Dylan has:", uniq_achiev((alice | bob | charlie), dylan))
    # print("Bob is missing:", no_achiev((dylan | alice | charlie), bob))
    # print("Charlie is missing:", no_achiev((dylan | bob | alice), charlie))
    # print("Dylan is missing:", no_achiev((alice | bob | charlie), dylan))
    print("\nOnly Alice has:", alice.difference(dylan | bob | charlie))
    print("Only Bob has:", bob.difference(dylan | alice | charlie))
    print("Only Charlie has:", charlie.difference(dylan | bob | alice))
    print("Only Dylan has:", dylan.difference(alice | bob | charlie))
    print("\nAlic is missing:", (dylan | bob | charlie).difference(alice))
    print("Bob is missing:", (dylan | alice | charlie).difference(bob))
    print("Charlie is missing:", (dylan | bob | alice).difference(charlie))
    print("Dylan is missing:", (alice | bob | charlie).difference(dylan))


if __name__ == "__main__":
    main()
