def gen_player_achievements():
    pass


def main() -> None:
    print("=== Achievement Tracker System ===")
    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon","MVP"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector","MVP"}
    charlie = {
        "level_10",
        "MVP",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }
    Dylan = {'Strategist',"MVP",'Speed Runner', 'Unstoppable', 'Untouchable', 'Boss Slayer'}
    print("Player Alice: ", alice)
    print("Player Bob: ", bob)
    print("Player Charlie: ", charlie)
    print("Player Dylan: ", Dylan)
    union = Dylan | alice | bob | charlie
    print("\nAll distinct achievements: ", union)
    intersection = alice & bob & charlie & Dylan
    print("\nCommon achievements:", intersection)

if __name__ == "__main__":
    main()