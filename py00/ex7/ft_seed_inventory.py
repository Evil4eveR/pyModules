def	ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == "area":
		print(f"{seed_type}.capitalize() seeds: covers {quantity} square meters")
	else:
		if unit == "packets":
			unit += " available"
		elif unit == "grams":
			unit += " total"
		else:
			unit = "unknown"
		print(f"{seed_type}.capitalize() seeds: {quantity} {unit}")
