def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0,
                'min_power': 0,
                'avg_power': 0.0
                }

    return {'max_power': max(mages, key=lambda x: x['power'])['power'],
            'min_power': min(mages, key=lambda x: x['power'])['power'],
            'avg_power': round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)  # noqa:E501
            }


def main() -> None:
    artifacts = [{'name': 'Fire Staff', 'power': 110, 'type': 'armor'},
                 {'name': 'Crystal Orb', 'power': 83, 'type': 'weapon'},
                 {'name': 'Ice Wand', 'power': 65, 'type': 'accessory'},
                 {'name': 'Lightning Rod', 'power': 76, 'type': 'relic'}
                 ]
    mages = [{'name': 'Zara', 'power': 84, 'element': 'light'},
             {'name': 'Zara', 'power': 68, 'element': 'wind'},
             {'name': 'Ember', 'power': 74, 'element': 'wind'},
             {'name': 'River', 'power': 95, 'element': 'fire'},
             {'name': 'Rowan', 'power': 72, 'element': 'fire'}
             ]
    spells = ['shield', 'freeze', 'lightning', 'fireball']
    print("\nTesting artifact sorter...")
    artifacts_sorted = artifact_sorter(artifacts)
    print(
        f"{artifacts_sorted[0]['name']}"
        f" ({artifacts_sorted[0]['power']} power)"
        f" comes before {artifacts_sorted[1]['name']}"
        f" ({artifacts_sorted[1]['power']} power)"
        )
    print("\nTesting power filter (min_power=80)...")
    mages_filter = power_filter(mages, 80)
    for mage in mages_filter:
        print(f"mage name: {mage['name']}, ({mage['power']} power)")
    print("\nTesting spell transformer...\n")
    spells_transformed = spell_transformer(spells)
    print(" ".join(spells_transformed))
    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(
        f"Max: {stats['max_power']},"
        f" Min: {stats['min_power']},"
        f" Avg: {stats['avg_power']}"
    )


if __name__ == "__main__":
    main()
