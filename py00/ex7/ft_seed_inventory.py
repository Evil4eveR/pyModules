# **************************************************************************** #
#																			  #
#														 :::	  ::::::::	#
#	ft_seed_inventory.py							   :+:	  :+:	:+:	#
#													 +:+ +:+		 +:+	  #
#	By: ymarmoud <ymarmoud@student.42.fr>		  +#+  +:+	   +#+		 #
#												 +#+#+#+#+#+   +#+			#
#	Created: 2026/04/09 16:37:14 by ymarmoud		  #+#	#+#			  #
#	Updated: 2026/04/09 20:43:57 by ymarmoud		 ###   ########.fr		#
#																			  #
# **************************************************************************** #

def	ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == "area":
		print(f"L{seed_type} seeds: covers {quantity} square meters")
	else:
		if unit == "packets":
			unit += " available"
		elif unit == "grams":
			unit += " total"
		else:
			unit = "unknown"
		print(f"{seed_type} seeds: {quantity} {unit}")